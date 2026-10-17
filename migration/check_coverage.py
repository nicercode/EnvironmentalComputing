"""Check that every page of the old site survives in its book chapter.

For each old page in migration/page-map.yml, counts the substantive lines
(prose and code, at least 25 characters) and how many appear in the mapped
chapter, ignoring formatting that the migration changes on purpose: chunk
option syntax, file paths, link targets and backtick style.

Exits non-zero if any page falls below the threshold, so it can run in CI.

Usage (from the repository root):
    python3 migration/check_coverage.py [--threshold 0.95]
"""
import argparse
import difflib
import os
import re
import subprocess
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUZZY = 0.8   # a line this similar to one in the chapter counts as present

# lines the migration drops deliberately
DROPPED = [
    re.compile(r"^\*\*Last updated:\*\*"),        # build-date stamps
    re.compile(r"^```\s*\{r"),                    # old chunk headers
]


def norm(line):
    line = re.sub(r"^\s*#+\s*", "", line)                 # heading level
    line = re.sub(r"</?(font|center)[^>]*>|\{fig-align=[^}]*\}", "", line)
    line = re.sub(r'<a id="[^"]*"></a>|\{#[^}]*\}', "", line)   # anchors
    line = re.sub(r"\]\([^)]*\)", "]", line)              # link targets
    line = re.sub(r"""(['"])[^'"\s]*/([^/'"\s]+)\1""", r"\1\2\1", line)
    line = re.sub(r"[`*_\s]+", " ", line)
    line = line.replace("Reshape2", "reshape2")
    return line.strip().lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=float, default=0.95)
    args = ap.parse_args()

    with open(os.path.join(ROOT, "migration", "page-map.yml")) as fh:
        cfg = yaml.safe_load(fh)
    ref = cfg["source_ref"]
    files = subprocess.run(["git", "-C", ROOT, "ls-tree", "-r", "--name-only",
                            ref], capture_output=True, text=True,
                           check=True).stdout.splitlines()

    def present(line, chapter, chapter_lines):
        n = norm(line)
        if n in chapter:
            return True
        # allow small edits (typo fixes, reworded link text)
        return any(difflib.SequenceMatcher(None, n, c).ratio() >= FUZZY
                   for c in chapter_lines
                   if abs(len(c) - len(n)) <= (1 - FUZZY) * len(n) + 10)

    failed = 0
    for c in cfg["chapters"]:
        with open(os.path.join(ROOT, "content", c["chapter"])) as fh:
            raw = fh.read()
        chapter = norm(raw.replace("\n", " "))
        chapter_lines = [norm(l) for l in raw.splitlines() if l.strip()]
        for s in c["sources"]:
            path = next(f for f in files if re.fullmatch(
                rf"content/{re.escape(s['page'])}/_index\.rmd", f, re.I))
            text = subprocess.run(["git", "-C", ROOT, "show", f"{ref}:{path}"],
                                  capture_output=True, text=True,
                                  check=True).stdout
            text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
            excepted = [e["starts"] for e in s.get("coverage_exceptions", [])]
            lines = [l for l in text.splitlines()
                     if len(l.strip()) >= 25
                     and not any(p.match(l.strip()) for p in DROPPED)
                     and not any(l.strip().startswith(e) for e in excepted)]
            missing = [l for l in lines
                       if not present(l, chapter, chapter_lines)]
            share = 1 - len(missing) / len(lines) if lines else 1
            flag = "" if share >= args.threshold else "  <-- BELOW THRESHOLD"
            print(f"{share:6.1%}  {len(lines):4d}  {s['page']:<58} "
                  f"-> {c['chapter']}{flag}")
            if flag:
                failed += 1
                for l in missing:
                    print(f"          missing: {l.strip()[:120]}")
    if failed:
        print(f"\n{failed} page(s) below {args.threshold:.0%}", file=sys.stderr)
        sys.exit(1)
    print("\nall pages above threshold")


if __name__ == "__main__":
    main()
