"""Port the old Hugo/blogdown tutorials into the Quarto book without losing
content.

For every chapter in migration/page-map.yml this script

1. converts the old page(s) (read from git, at `source_ref`) to Quarto
   markdown: chunk options to `#|` form, headings nested under a `##`
   section when several pages are merged, image/data paths rewritten and the
   files copied next to the chapter;
2. aligns that faithful conversion, paragraph by paragraph, with the chapter
   as it already exists on this branch: where both have a matching block the
   existing (edited) version is kept, blocks missing from the existing
   chapter are restored in place, and blocks only in the existing chapter
   are kept;
3. rewrites links to old site URLs into links between chapters;
4. writes `_redirects` (Netlify) so every old URL, including the
   WordPress-era aliases, lands on its new chapter/section.

A report of everything restored or needing review goes to
migration/report.md.

Usage (from the repository root):
    python3 migration/migrate.py
"""
import collections
import difflib
import os
import posixpath
import re
import subprocess
import sys
from collections import defaultdict

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
MATCH_THRESHOLD = 0.5
STUB_MAX_LINES = 6
# a fenced code block opens/closes on a line holding only the fence and an
# optional language; "```code```" on one line is inline code, not a fence
FENCE = re.compile(r"^\s*(`{3,})\s*(\{[^}]*\}|[\w+-]*)\s*$")
# a branch block counts as a rewrite of an old one when this share of its
# words appear in the old text
REWRITE_OVERLAP = 0.6
# a matched branch block shorter than this fraction of the old one has been
# trimmed, and the old text is restored
TRIMMED = 0.85
# build-date stamps: they show when the page was rendered, not edited
LAST_UPDATED = re.compile(r"^\*\*Last updated:\*\*\s*`r format\(Sys\.time\(\).*$",
                          re.M)


# --------------------------------------------------------------------------
# git access to the old site
# --------------------------------------------------------------------------

def git(*args, binary=False):
    out = subprocess.run(["git", "-C", ROOT, *args], capture_output=True,
                         check=True)
    return out.stdout if binary else out.stdout.decode("utf-8")


class OldSite:
    def __init__(self, ref):
        self.ref = ref
        self.files = set(git("ls-tree", "-r", "--name-only", ref).splitlines())
        self.files_lower = {f.lower(): f for f in self.files}
        self.pages = {}
        for f in self.files:
            m = re.match(r"content/(.+)/_index\.rmd$", f, re.I)
            if m:
                self.pages[m.group(1)] = f

    def read(self, path):
        return git("show", f"{self.ref}:{path}")

    def read_bytes(self, path):
        return git("show", f"{self.ref}:{path}", binary=True)

    def page(self, page):
        text = self.read(self.pages[page])
        m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
        meta = yaml.safe_load(m.group(1)) if m else {}
        return meta or {}, text[m.end():] if m else text


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def exists_exact(path):
    """os.path.exists, but case-sensitive even on macOS: the site is built on
    Linux, where "x.jpg" does not find "x.JPG"."""
    path = os.path.normpath(path)
    if not os.path.exists(path):
        return False
    parent, name = os.path.split(path)
    if not name:
        return True
    return name in os.listdir(parent or ".") and \
        (not parent or parent == os.sep or exists_exact(parent))


def real_case(path):
    """The path of an existing file with the letter case it has on disk, or
    None if there is no such file (in any case)."""
    path = os.path.normpath(path)
    parent, name = os.path.split(path)
    # not os.path.isdir: on macOS that is true for a folder in the wrong case
    if parent and not exists_exact(parent):
        parent = real_case(parent)
        if parent is None:
            return None
    try:
        names = os.listdir(parent or ".")
    except FileNotFoundError:
        return None
    match = [n for n in names if n.lower() == name.lower()]
    if name in match:
        return os.path.join(parent, name) if parent else name
    return os.path.join(parent, match[0]) if match else None


def pandoc_id(text):
    """Identifier pandoc gives a heading (auto_identifiers extension)."""
    text = re.sub(r"\{#([^}]+)\}\s*$", "", text).strip()
    s = text.lower()
    s = re.sub(r"[^\w\s.-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"^[^a-z]+", "", s)
    return s or "section"


LIST_ITEM = re.compile(r"^([*+-]|\d+[.)])\s+\S")


def blank_line_before_lists(text):
    """Pandoc only starts a list after a blank line. The old site's parser
    didn't need one, so "Intro:\\n* item" rendered there as a list but here
    as one paragraph with literal asterisks."""
    out, in_code, in_list = [], False, False
    for line in text.splitlines():
        if FENCE.match(line):
            in_code = not in_code
        elif not in_code:
            if not line.strip():
                in_list = False
            elif LIST_ITEM.match(line):
                # a list item further down a list (or after a list item that
                # wraps onto unindented lines) needs nothing
                if out and out[-1].strip() and not in_list:
                    out.append("")
                in_list = True
        out.append(line)
    return "\n".join(out)


def seed_chunk(seed):
    """A hidden chunk fixing the random number seed, so re-running a chapter
    reproduces its output (and its frozen figures)."""
    return f"```{{r}}\n#| include: false\nset.seed({seed})\n```"


def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return None, text
    return m.group(0), text[m.end():]


def is_stub(text):
    _, body = split_front_matter(text)
    body = body.strip()
    return not body or body == "Placeholder content." or \
        len(text.strip().splitlines()) <= STUB_MAX_LINES


def old_url(page):
    return "/" + page.lower().strip("/") + "/"


def norm_url(u):
    u = u.split("#")[0].strip()
    u = re.sub(r"^(/\.\.)+", "", u)          # "/../statistics/x" -> "/statistics/x"
    u = posixpath.normpath("/" + u.strip("/")).lower()
    return u if u == "/" else u + "/"


def chunk_option_value(v):
    v = v.strip()
    if v in ("T", "TRUE"):
        return "true"
    if v in ("F", "FALSE"):
        return "false"
    if re.fullmatch(r"-?\d+(\.\d+)?", v):
        return v
    m = re.fullmatch(r"""(['"])(.*)\1""", v)
    if m:
        s = m.group(2)
        return s if re.fullmatch(r"[\w.-]+", s) and s not in ("true", "false") \
            else '"' + s.replace('"', '\\"') + '"'
    return "!expr " + v


OPTION_NAMES = {"fig.width": "fig-width", "fig.height": "fig-height",
                "out.width": "out-width", "out.height": "out-height",
                "fig.cap": "fig-cap", "fig.align": "fig-align"}


def split_options(s):
    """Split a knitr option string on top-level commas."""
    parts, depth, quote, cur = [], 0, None, ""
    for ch in s:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
        elif ch in "'\"":
            quote = ch
            cur += ch
        elif ch in "([":
            depth += 1
            cur += ch
        elif ch in ")]":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    return [p.strip() for p in parts if p.strip()]


# --------------------------------------------------------------------------
# blocks: the unit of alignment
# --------------------------------------------------------------------------

class Block:
    def __init__(self, text, kind, origin=None):
        self.text = text            # markdown, without trailing newline
        self.kind = kind            # "code", "heading" or "text"
        self.origin = origin        # old page this block came from (if known)
        self.key = self._key()

    @property
    def words(self):
        return set(w for w in self.key.split() if len(w) >= 3)

    def _key(self):
        t = self.text
        if self.kind == "code":
            lines = [l for l in t.splitlines()[1:-1] if not l.startswith("#|")]
            t = "\n".join(lines)
        else:
            t = re.sub(r"\]\([^)]*\)", "]", t)        # drop link targets
            t = re.sub(r"\{#[^}]*\}", "", t)
        return re.sub(r"\W+", " ", t).strip().lower()


def to_blocks(text, origin=None):
    blocks, cur, lines = [], [], text.splitlines()
    i = 0

    def flush():
        if cur:
            blocks.append(Block("\n".join(cur), "text", origin))
            cur.clear()

    while i < len(lines):
        line = lines[i]
        if FENCE.match(line):
            flush()
            fence = FENCE.match(line).group(1)
            j = i + 1
            while j < len(lines) and not re.match(r"^\s*" + fence + r"\s*$",
                                                   lines[j]):
                j += 1
            blocks.append(Block("\n".join(lines[i:j + 1]), "code", origin))
            i = j + 1
            continue
        if re.match(r"^#{1,6}\s", line):
            flush()
            blocks.append(Block(line, "heading", origin))
        elif not line.strip():
            flush()
        else:
            cur.append(line)
        i += 1
    flush()
    return blocks


def similarity(a, b):
    if a.kind != b.kind:
        return 0.0
    if a.key == b.key:
        return 1.0
    if not a.key or not b.key:
        return 0.0
    short, long_ = sorted((a.key, b.key), key=len)
    if len(short) >= 40 and short in long_:
        return 0.9
    if a.kind == "heading":
        return 0.0
    sm = difflib.SequenceMatcher(None, a.key, b.key, autojunk=False)
    if sm.real_quick_ratio() < MATCH_THRESHOLD or \
            sm.quick_ratio() < MATCH_THRESHOLD:
        return 0.0
    return sm.ratio()


def tidy_markdown(body, log, sectioned=False):
    """Fix markup the old site's renderer tolerated (or rendered wrongly
    too) but Pandoc doesn't, outside code chunks."""
    out, in_code, changed = [], False, collections.Counter()
    for line in body.split("\n"):
        if FENCE.match(line):
            in_code = not in_code
        elif not in_code:
            # "###Heading": Pandoc needs a space after the #s
            new = re.sub(r"^(#{1,6})([^#\s])", r"\1 \2", line)
            # <font face="monospace">x</font> -> `x`
            new = re.sub(r'<font face="monospace">(.*?)</font>', r"`\1`", new)
            # <center>![](img)</center> -> centred figure
            new = re.sub(r"<center>\s*(!\[[^\]]*\]\([^)]+\))\s*</center>",
                         r'\1{fig-align="center"}', new)
            if new != line:
                changed["heading space" if new.startswith("#") and
                        not line.startswith("# ") and "font" not in line
                        else "<font>/<center> tags"] += 1
            line = new
        out.append(line)
    body = "\n".join(out)

    # chapters start their sections at ##; a chapter starting at ### gets
    # numbered "N.0.1"
    levels, in_code = [], False
    for line in body.split("\n"):
        if FENCE.match(line):
            in_code = not in_code
        elif not in_code and (m := re.match(r"^(#{2,6})\s", line)):
            levels.append(len(m.group(1)))
    if not sectioned and levels and levels[0] > 2 and 2 in levels:
        # a single old page whose sections are ###, with the odd stray ##
        # among them (e.g. "## Assumptions to check" between ### siblings):
        # make the strays siblings too
        out, in_code = [], False
        for line in body.split("\n"):
            if FENCE.match(line):
                in_code = not in_code
            elif not in_code and re.match(r"^##\s", line):
                line = "#" + line
            out.append(line)
        body = "\n".join(out)
        levels = [3 if l == 2 else l for l in levels]
        changed["stray ## made siblings of ###"] += 1
    if levels and min(levels) > 2:
        shift = min(levels) - 2
        out, in_code = [], False
        for line in body.split("\n"):
            if FENCE.match(line):
                in_code = not in_code
            elif not in_code and (m := re.match(r"^(#{3,6})(\s.*)$", line)):
                line = "#" * (len(m.group(1)) - shift) + m.group(2)
            out.append(line)
        body = "\n".join(out)
        changed["headings raised to start at ##"] += 1

    for what, n in changed.items():
        log.append(f"edit applied: tidied markup ({what}: {n})")
    return body


def keep_spelling_fixes(old, new):
    """Return `old` text with single-word corrections made in `new` applied
    (e.g. "Indpendence" -> "Independence"), so restoring trimmed text
    doesn't undo the first conversion's typo fixes."""
    tok_old = re.findall(r"\s+|[^\s]+", old)
    words_old = [i for i, t in enumerate(tok_old) if not t.isspace()]
    w_old = [tok_old[i] for i in words_old]
    w_new = new.split()
    sm = difflib.SequenceMatcher(None, w_old, w_new, autojunk=False)
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op != "replace" or a2 - a1 != b2 - b1:
            continue
        for a, b in zip(range(a1, a2), range(b1, b2)):
            x, y = w_old[a], w_new[b]
            if re.fullmatch(r"[A-Za-z'’]+[.,;:]?", x) and \
                    re.fullmatch(r"[A-Za-z'’]+[.,;:]?", y) and \
                    difflib.SequenceMatcher(None, x, y).ratio() >= 0.75:
                tok_old[words_old[a]] = y
    return "".join(tok_old)


def align(F, D):
    """Monotonic alignment maximising total similarity (gaps cost nothing).
    Returns a list of (i, j) pairs, with None for unmatched blocks."""
    n, m = len(F), len(D)
    sim = {}
    for i in range(n):
        for j in range(m):
            s = similarity(F[i], D[j])
            if s >= MATCH_THRESHOLD:
                sim[i, j] = s
    score = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            best = max(score[i + 1][j], score[i][j + 1])
            if (i, j) in sim:
                best = max(best, sim[i, j] + score[i + 1][j + 1])
            score[i][j] = best
    pairs, i, j = [], 0, 0
    while i < n and j < m:
        if (i, j) in sim and \
                abs(score[i][j] - (sim[i, j] + score[i + 1][j + 1])) < 1e-9:
            pairs.append((i, j))
            i, j = i + 1, j + 1
        elif score[i][j] == score[i + 1][j]:
            pairs.append((i, None))
            i += 1
        else:
            pairs.append((None, j))
            j += 1
    pairs += [(k, None) for k in range(i, n)]
    pairs += [(None, k) for k in range(j, m)]
    return pairs


# --------------------------------------------------------------------------
# converting an old page
# --------------------------------------------------------------------------

class Chapter:
    def __init__(self, spec, site, all_specs):
        self.spec = spec
        self.site = site
        self.path = spec["chapter"]
        self.dir = posixpath.dirname(self.path)
        self.is_folder_page = posixpath.basename(self.path) == "index.qmd"
        self.sectioned = any("section" in s for s in spec["sources"])
        self.labels = set()
        self.copied = []
        self.log = []

    # -- assets --------------------------------------------------------------
    def asset_target(self, basename):
        """Where (relative to the chapter) an asset should live. Reuse a copy
        that already exists in this part of the book.

        Each part keeps its own copy, rather than every chapter reading the
        one in datasets/, so the code readers copy keeps short paths. The
        copies are not all the same file: the old site had different
        versions under one name (Herbivore_specialisation.csv has three, with
        different columns), and each chapter's code expects its own, so
        don't merge them without checking the chapters."""
        part = self.dir.split("/")[0]
        for dirpath, _, files in os.walk(os.path.join(CONTENT, part)):
            if basename in files:
                rel = os.path.relpath(os.path.join(dirpath, basename),
                                      os.path.join(CONTENT, self.dir))
                return rel.replace(os.sep, "/"), None
        if self.is_folder_page:
            rel = basename
        elif os.path.splitext(basename)[1].lower() in IMAGE_EXT:
            rel = "images/" + basename
        else:
            rel = "data/" + basename
        return rel, rel

    def rewrite_asset(self, page, ref):
        """Map a path used on an old page to the chapter's copy of the file.
        Returns None if `ref` isn't a file belonging to the old page."""
        if re.match(r"^(https?:|/|#|mailto:)", ref) or not ref:
            return None
        src = posixpath.normpath(f"content/{page}/{ref}")
        # the old site was built on case-insensitive filesystems, so
        # "x.jpg" may name "x.JPG"; use the file's real name
        src = self.site.files_lower.get(src.lower())
        if src is None:
            return None
        rel, to_copy = self.asset_target(posixpath.basename(src))
        if to_copy:
            dest = os.path.join(CONTENT, self.dir, to_copy)
            if not exists_exact(dest):
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as fh:
                    fh.write(self.site.read_bytes(src))
                self.copied.append(f"{self.dir}/{to_copy}")
        return rel

    # -- one old page -> markdown -------------------------------------------
    def convert(self, page, section):
        meta, body = self.site.page(page)
        slug = page.split("/")[-1].lower()
        body = body.replace("library(Reshape2)", "library(reshape2)")
        body = LAST_UPDATED.sub("", body)

        lines = body.splitlines()
        # heading levels used outside code chunks (inside, "#" is a comment)
        levels, in_code = [], False
        for l in lines:
            if FENCE.match(l):
                in_code = not in_code
            elif not in_code and (m := re.match(r"^(#{1,6})\s", l)):
                levels.append(len(m.group(1)))
        base = 3 if self.sectioned else 2
        shift = base - min(levels) if levels else 0

        out, in_code, n_chunk = [], False, 0
        if section:
            out += [f"## {section}", ""]
        for l in lines:
            m = re.match(r"^(\s*)```\s*\{r([^}]*)\}\s*$", l)
            if m and not in_code:
                in_code = True
                n_chunk += 1
                opts = split_options(m.group(2).lstrip(" ,"))
                label = None
                if opts and "=" not in opts[0]:
                    label = opts.pop(0).strip("'\"")
                label = f"{slug}-{label or n_chunk}"
                while label in self.labels:
                    label += "-b"
                self.labels.add(label)
                out.append(m.group(1) + "```{r}")
                out.append(f"#| label: {label}")
                for o in opts:
                    if "=" not in o:
                        continue
                    k, v = o.split("=", 1)
                    k = OPTION_NAMES.get(k.strip(), k.strip())
                    out.append(f"#| {k}: {chunk_option_value(v)}")
                continue
            if FENCE.match(l):
                in_code = not in_code
                out.append(l)
                continue
            if not in_code and (h := re.match(r"^(#{1,6})(\s.*)$", l)):
                lvl = max(2, min(6, len(h.group(1)) + shift))
                l = "#" * lvl + h.group(2)
            l = self.rewrite_paths(page, l)
            out.append(l)
        return meta, "\n".join(out).strip("\n")

    def rewrite_paths(self, page, line):
        def md(m):
            new = self.rewrite_asset(page, m.group(2))
            return m.group(0) if new is None else f"{m.group(1)}({new}{m.group(3)})"

        def quoted(m):
            new = self.rewrite_asset(page, m.group(2))
            return m.group(0) if new is None else f"{m.group(1)}{new}{m.group(1)}"

        line = re.sub(r"(!?\[[^\]]*\])\(([^)\s]+)([^)]*)\)", md, line)
        line = re.sub(r"""(['"])([^'"\s]+\.\w{1,6})\1""", quoted, line)
        return line


# --------------------------------------------------------------------------
# links
# --------------------------------------------------------------------------

class LinkMap:
    def __init__(self):
        self.urls = {}       # old url -> (chapter path, anchor or None)

    def add(self, url, chapter, anchor):
        self.urls.setdefault(norm_url(url), (chapter, anchor))

    def resolve(self, target, chapter, origins):
        """Rewrite one link target found in `chapter`. `origins` are old pages
        relative links may have been written against."""
        url, _, frag = target.partition("#")
        if re.match(r"^(https?:|mailto:|#)", target) or url.endswith(".qmd") \
                or not url:
            return None
        here = posixpath.dirname(chapter)
        if m := re.match(r"^/datasets/([^/]+\.\w+)/?$", url):
            return posixpath.relpath("../datasets/" + m.group(1), here)
        if not url.startswith("/"):
            # a relative link between book chapters, written without .qmd
            # (relative to the chapter's folder, or to the chapter as if it
            # were a folder, as on the old site where each page was one)
            for base in (here, re.sub(r"(/index)?\.qmd$", "", chapter)):
                p = posixpath.normpath(posixpath.join(base, url.rstrip("/")))
                for cand in (p + ".qmd", p + "/index.qmd"):
                    if exists_exact(os.path.join(CONTENT, cand)):
                        return posixpath.relpath(cand, here) + \
                            ("#" + frag if frag else "")
        candidates = []
        if url.startswith("/"):
            candidates.append(url)
        else:
            for o in origins:
                candidates.append(posixpath.join(old_url(o), url))
        for c in candidates:
            hit = self.urls.get(norm_url(c))
            if not hit:
                # links that were already broken on the old site, e.g.
                # "/graphics/cluster-analysis/": match on the last segment
                last = norm_url(c).rstrip("/").split("/")[-1]
                same = {v for k, v in self.urls.items()
                        if k.rstrip("/").split("/")[-1] == last}
                hit = same.pop() if len(same) == 1 else None
            if hit:
                dest, anchor = hit
                anchor = frag or anchor
                if dest == chapter:
                    return "#" + anchor if anchor else \
                        posixpath.basename(chapter)
                rel = posixpath.relpath(dest, here)
                return rel + ("#" + anchor if anchor else "")
        return "UNRESOLVED"


def rewrite_links(text, chapter, origins, links, log):
    out, in_code = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_code = not in_code
        if not in_code:
            def sub(m):
                new = links.resolve(m.group(2), chapter, origins)
                if new == "UNRESOLVED":
                    log.append(f"unresolved link `{m.group(2)}`")
                    return m.group(0)
                if new is None:
                    return m.group(0)
                return f"{m.group(1)}({new})"
            line = re.sub(r"(?<!!)(\[[^\]]*\])\(([^)\s]+)\)", sub, line)
        out.append(line)
    return "\n".join(out)


# --------------------------------------------------------------------------
# preface: credits and the migration table
# --------------------------------------------------------------------------

def fix_preface(text, specs, site):
    # editors and page authors from the old "About" page go before the
    # acknowledgements; the old shortcode-driven contributor list is replaced
    # by the generated one already in the chapter
    m = re.search(r"\*\*Site editors:\*\*.*?(?=\n## Contributors)", text, re.S)
    if m:
        credits = m.group(0).strip()
        text = text[:m.start()] + text[m.end():]
        text = re.sub(r"\n## Contributors\n+Thanks to them <i [^\n]*\n?", "\n",
                      text)
        text = text.replace("\n## Acknowledgments\n",
                            "\n## Editors and authors\n\n" + credits +
                            "\n\n## Acknowledgments\n", 1)

    # the migration table, generated from the page map so it matches the
    # redirects
    rows = []
    for c in specs:
        current = None
        for s in c["sources"]:
            current = s.get("section", current)
            dest = posixpath.relpath(c["chapter"], ".")
            label = re.sub(r"(/index)?\.qmd$", "", c["chapter"])
            anchor = "#" + pandoc_id(current) if current else ""
            where = f"[{label}]({dest}{anchor})" + \
                (f", section *{current}*" if current else "")
            rows.append(f"| `{old_url(s['page'])}` | {where} |")
    table = ("| Old page | Now in |\n|---|---|\n" + "\n".join(rows))
    text = re.sub(
        r"Key structural changes:\n.*?(?=\n### 2022 migration)",
        "The old site had one page per topic. In the book, related pages "
        "are combined into chapters (for example, the three mixed-model "
        "pages are now one chapter with three sections), grouped into parts. "
        "Every old address redirects to its new chapter and section.\n\n"
        "Page migration table:\n\n" + table + "\n", text, flags=re.S)

    # an alias for a page that had already been removed from the old site
    text = re.sub(r"^- \[/making-maps-of-your-study-sites/\]\([^)]*\)\n", "",
                  text, flags=re.M)
    return text


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    with open(os.path.join(ROOT, "migration", "page-map.yml")) as fh:
        cfg = yaml.safe_load(fh)
    site = OldSite(cfg["source_ref"])
    base_site = OldSite(cfg["base_ref"])
    specs = cfg["chapters"]

    # every old page mapped exactly once
    mapped = [s["page"] for c in specs for s in c["sources"]]
    dupes = {p for p in mapped if mapped.count(p) > 1}
    missing = set(site.pages) - set(mapped)
    unknown = set(mapped) - set(site.pages)
    if dupes or missing or unknown:
        for label, items in (("listed twice", dupes),
                             ("not mapped", missing),
                             ("not on the old site", unknown)):
            for p in sorted(items):
                print(f"ERROR: {p}: {label}", file=sys.stderr)
        sys.exit(1)

    branch_files = set(git("ls-tree", "-r", "--name-only",
                           cfg["branch_ref"]).splitlines())
    links, redirects = LinkMap(), []
    links.add("/", "../index.qmd", None)
    for c in specs:
        current = None
        for s in c["sources"]:
            if "section" in s:
                current = pandoc_id(s["section"])
            anchor = current
            meta, _ = site.page(s["page"])
            aliases = meta.get("aliases") or []
            if isinstance(aliases, str):
                aliases = [aliases]
            for u in [old_url(s["page"])] + aliases:
                links.add(u, c["chapter"], anchor)
            html = "/content/" + re.sub(r"(index)?\.qmd$", "", c["chapter"])
            html = html if html.endswith("/") else html + ".html"
            for u in [old_url(s["page"])] + aliases:
                u = norm_url(u)
                if u != "/":
                    redirects.append((u, html + ("#" + anchor if anchor else "")))

    link_fix_used = set()
    report = ["# Migration report", "",
              f"Old site: `{cfg['source_ref']}` ({len(site.pages)} pages). "
              f"Book chapters written: {len(specs)}.", ""]
    for c in specs:
        ch = Chapter(c, site, specs)
        path = os.path.join(CONTENT, ch.path)
        prefer_old = c.get("prefer") == "old"
        # the chapter as the first conversion left it (read from git so the
        # script can be re-run over its own output)
        branch_file = "content/" + c.get("replaces", ch.path)
        existing = git("show", f"{cfg['branch_ref']}:{branch_file}") \
            if branch_file in branch_files else ""
        fm, existing_body = split_front_matter(existing)
        D = [] if is_stub(existing) else to_blocks(existing_body)

        F, metas = [], []
        for s in c["sources"]:
            meta, md = ch.convert(s["page"], s.get("section"))
            metas.append(meta)
            F += to_blocks(md, origin=s["page"])

        pairs = align(F, D)
        out, restored, kept_new, dropped, trimmed = [], [], [], [], []
        gap_f, gap_d = [], []
        old_words = set().union(*(b.words for b in F)) if F else set()

        def rewrite_of(b, pool_words):
            w = b.words
            return bool(w) and len(w & pool_words) / len(w) >= REWRITE_OVERLAP

        def close_gap():
            # a renamed heading: one heading on each side at the same level
            hf = [b for b in gap_f if b.kind == "heading"]
            hd = [b for b in gap_d if b.kind == "heading"]
            if len(hf) == 1 and len(hd) == 1 and \
                    hf[0].text.split()[0] == hd[0].text.split()[0] and \
                    not prefer_old:
                gap_f.remove(hf[0])
            # branch blocks that just reword old blocks of the same gap (or,
            # with prefer: old, any old block) are condensed rewrites: the
            # old text replaces them. Anything else is new writing and stays.
            pool = old_words if prefer_old else \
                set().union(*(b.words for b in gap_f)) if gap_f else set()
            for b in gap_d:
                if LAST_UPDATED.fullmatch(b.text.strip()):
                    continue          # build-date stamp, removed below
                if gap_f or prefer_old:
                    if rewrite_of(b, pool) and b.kind != "heading" or \
                            prefer_old and b.kind == "heading" and \
                            any(f.kind == "heading" for f in gap_f):
                        dropped.append(b)
                        continue
                out.append(b)
                kept_new.append(b)
            for b in gap_f:
                out.append(b)
                restored.append(b)
            gap_f.clear()
            gap_d.clear()

        # the old pages as they were when the first conversion was made:
        # text changed on the old site since then (e.g. a correction) must
        # win over the first conversion's copy of the earlier text
        base_keys = set()
        base_ch = Chapter(c, base_site, specs)
        for s in c["sources"]:
            if s["page"] in base_site.pages:
                _, md = base_ch.convert(s["page"], s.get("section"))
                base_keys |= {b.key for b in to_blocks(md)}
        updated = []

        for i, j in pairs:
            if i is not None and j is not None:
                close_gap()
                f, d = F[i], D[j]
                d.origin = f.origin
                if f.key not in base_keys and f.key != d.key and \
                        f.origin in base_site.pages:
                    out.append(f)
                    updated.append(f)
                elif prefer_old and f.key != d.key or \
                        len(d.key) < TRIMMED * len(f.key):
                    if f.kind == "text":
                        f.text = keep_spelling_fixes(f.text, d.text)
                    out.append(f)
                    if not prefer_old:
                        trimmed.append((f, d))
                else:
                    out.append(d)
            elif i is not None:
                gap_f.append(F[i])
            else:
                gap_d.append(D[j])
        close_gap()

        # front matter: keep the branch's, else build from the old page;
        # `title:` in the page map overrides either
        if not fm or c.get("title"):
            title = c.get("title") or metas[0].get("title", "")
            fm = "---\ntitle: " + yaml.safe_dump(title).strip().replace(
                "\n...", "") + "\n---\n"
        body = "\n\n".join(b.text for b in out)
        if c.get("unnumbered"):
            # top-level chapters take their heading from the body, so the
            # book can leave it out of the chapter numbering
            m = re.search(r"^title:\s*(.+)$", fm, re.M)
            heading = yaml.safe_load(m.group(1))
            fm = fm.replace(m.group(0), "pagetitle: " + m.group(1))
            body = f"# {heading} {{.unnumbered}}\n\n" + body
        body = tidy_markdown(body, ch.log, ch.sectioned)
        body = LAST_UPDATED.sub("", body)
        body = re.sub(r"\n{3,}", "\n\n", body)
        if ch.path == "preface.qmd":
            body = fix_preface(body, specs, site)
        origins = [s["page"] for s in c["sources"]]
        body = rewrite_links(body, ch.path, origins, links, ch.log)
        # dead external links, fixed in every chapter
        for k, e in enumerate(cfg.get("link_fixes", [])):
            n = body.count(e["old"])
            if n:
                body = body.replace(e["old"], e["new"]) if e.get("all") \
                    else body.replace(e["old"], e["new"], 1)
                link_fix_used.add(k)
                ch.log.append(f"edit applied: {e['reason']}")
        for e in c.get("edits", []):
            # match ignoring trailing spaces on each line (markdown line
            # breaks, which YAML block scalars don't keep)
            # (only at line ends inside the match, not after its last line)
            parts = e["old"].split("\n")
            pattern = "".join(re.escape(l.rstrip()) + r"[ \t]*\n"
                              for l in parts[:-1]) + re.escape(parts[-1])
            body, n = re.subn(pattern, lambda _: e["new"], body,
                              count=0 if e.get("all") else 1)
            if not n:
                sys.exit(f"ERROR: {ch.path}: edit not applicable "
                         f"({e['reason']}): {e['old'][:60]!r}")
            ch.log.append(f"edit applied: {e['reason']}")
        body = blank_line_before_lists(body)
        if "seed" in c:
            body = seed_chunk(c["seed"]) + "\n\n" + body.lstrip("\n")

        old_path = os.path.join(CONTENT, c.get("replaces", ch.path))
        if old_path != path and os.path.exists(old_path):
            os.remove(old_path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as fh:
            fh.write(fm.rstrip("\n") + "\n\n" + body.strip("\n") + "\n")

        # check every local file the chapter refers to exists, with the same
        # letter case (fixing references that only worked on macOS)
        refs = re.findall(r"!?\[[^\]]*\]\(([^)\s#]+)", body) + \
            re.findall(r"""src=["']([^"']+)["']""", body) + \
            re.findall(r"""['"]((?:\.\./|images/|data/)[^'"\s]+)['"]""", body)
        for ref in sorted(set(refs)):
            if re.match(r"^(https?:|/|mailto:)", ref):
                continue
            full = os.path.join(CONTENT, ch.dir, ref)
            if exists_exact(full):
                continue
            fixed = real_case(full)
            if fixed:
                new_ref = os.path.relpath(fixed, os.path.join(CONTENT, ch.dir))
                body = body.replace(ref, new_ref)
                ch.log.append(f"edit applied: letter case `{ref}` -> "
                              f"`{new_ref}` (only worked on macOS)")
            else:
                ch.log.append(f"missing file `{ref}`")
        with open(path, "w") as fh:
            fh.write(fm.rstrip("\n") + "\n\n" + body.strip("\n") + "\n")

        report.append(f"## {ch.path}")
        report.append(
            f"{len(F)} blocks from {len(c['sources'])} old page(s). "
            + ("Existing chapter was a placeholder: written from the old "
               "page(s)." if not D else
               f"{len(F) - len(restored)} matched the first conversion; "
               f"**{len(restored)} restored** (missing), "
               f"**{len(trimmed)} restored** (trimmed), "
               f"**{len(updated)} updated** (changed on the old site since "
               f"the first conversion), "
               f"{len(dropped)} condensed rewrites replaced by the original, "
               f"{len(kept_new)} new blocks kept."
               + (" Original wording preferred throughout." if prefer_old
                  else "")))
        if ch.copied:
            report.append(f"\nCopied files: {', '.join(ch.copied)}")
        report.append("")
        for line in ch.log:
            report.append(f"- EDIT: {line[len('edit applied: '):]}"
                          if line.startswith("edit applied: ")
                          else f"- REVIEW: {line}")
        if D and (restored or trimmed or dropped or kept_new or updated):
            report.append("\n<details><summary>Details</summary>\n")
            for b in updated:
                report.append(f"- updated `{b.origin}`: "
                              f"{b.text.splitlines()[0][:110]}")
            for b in restored:
                report.append(f"- restored `{b.origin}`: "
                              f"{b.text.splitlines()[0][:110]}")
            for f, d in trimmed:
                report.append(f"- untrimmed `{f.origin}`: "
                              f"{f.text.splitlines()[0][:110]}")
            for b in dropped:
                report.append(f"- replaced rewrite: "
                              f"{b.text.splitlines()[0][:110]}")
            for b in kept_new:
                report.append(f"- kept new: {b.text.splitlines()[0][:110]}")
            report.append("\n</details>")
        report.append("")

    for k, e in enumerate(cfg.get("link_fixes", [])):
        if k not in link_fix_used:
            sys.exit(f"ERROR: link fix not applicable ({e['reason']}): "
                     f"{e['old'][:60]!r}")

    # data files previously served at /datasets/
    for f in sorted(site.files):
        if f.startswith("static/datasets/"):
            dest = os.path.join(ROOT, "datasets", f.split("/")[-1])
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as fh:
                fh.write(site.read_bytes(f))

    with open(os.path.join(ROOT, "_redirects"), "w") as fh:
        fh.write("# Old site URLs -> book chapters. "
                 "Generated by migration/migrate.py\n")
        for old, new in sorted(set(redirects)):
            fh.write(f"{old}  {new}  301\n")

    with open(os.path.join(ROOT, "migration", "report.md"), "w") as fh:
        fh.write("\n".join(report) + "\n")
    print(f"wrote {len(specs)} chapters, {len(set(redirects))} redirects; "
          "see migration/report.md")


if __name__ == "__main__":
    main()
