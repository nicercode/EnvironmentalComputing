# Migrating the old Hugo site into the Quarto book

The scripts here ported the 73 pages of the old Hugo/blogdown site into the
book's chapters without losing content, and generate the redirects from the
old addresses. They can be re-run, but read "Before you re-run" first.

| File | Purpose |
| --- | --- |
| `page-map.yml` | Maps every old page to a chapter and section; holds all deliberate edits |
| `migrate.py` | Rebuilds the chapters listed in the map and writes `_redirects` and `report.md` |
| `check_coverage.py` | Checks each old page survives in its chapter (at least 95% of its lines) |
| `check_redirects.py` | Checks every `_redirects` destination exists in the built book, anchor included |
| `report.md` | Generated list of every restored passage and edit, for review |

## Set up

You need Python 3 with PyYAML, and a clone of this repository with **full
history**. Use a virtual environment so PyYAML stays out of your system Python:

```sh
python3 -m venv .venv-migration
.venv-migration/bin/pip install pyyaml
```

(Add `.venv-migration/` to `.git/info/exclude` if you don't want it showing in
`git status`.)

The old site is read from git, not from the working tree. `page-map.yml` pins
three commits, and all three must exist locally:

| Key | What it is |
| --- | --- |
| `source_ref` | The old site, including the latest fixes made to it. Old pages are read from here |
| `branch_ref` | The first Quarto conversion. Existing chapters are read from here (see below) |
| `base_ref` | The old site as it was when that conversion was made, so text changed on the old site since then wins over the conversion |

If a script fails with a git "bad object" or "unknown revision" error, fetch
the history: `git fetch --all --tags`, and `git fetch --unshallow` if the clone
is shallow. CI uses `fetch-depth: 0` for the same reason.

## Before you re-run

**`migrate.py` rebuilds each chapter listed in `page-map.yml` and overwrites
`content/<chapter>`.** It aligns the old page with the chapter as it was at
`branch_ref`, a pinned historical commit, not with the file in your working
tree. So **any change made to a mapped chapter since then, by hand or by
another tool, is lost on the next run** unless it is recorded in
`page-map.yml`. Record fixes in the map instead of (or as well as) editing the
chapter:

- `edits`: exact find/replace on the merged text, each with a `reason`. The run
  stops if the text isn't found.
- `link_fixes`: replacements for dead links, applied to every chapter.
- `title`, `unnumbered`, `seed`, `prefer`, `coverage_exceptions`: other
  per-chapter options. The comment at the top of `page-map.yml` explains each.

Chapters that aren't in the map (for example `content/contributing.qmd`) are
never touched.

A safe habit: run `migrate.py` on a clean working tree and read
`git diff content/`. If it changes something you didn't expect, a fix is
missing from the map.

## Re-running and validating

From the repository root:

```sh
# 1. rebuild the chapters, _redirects and migration/report.md
.venv-migration/bin/python migration/migrate.py

# 2. confirm every old page still survives in its chapter
.venv-migration/bin/python migration/check_coverage.py

# 3. render the book (re-runs the code of changed chapters, refreshes _freeze/)
quarto render

# 4. confirm every redirect lands on a real page and section
.venv-migration/bin/python migration/check_redirects.py

# 5. (optional) check internal links and section anchors, as CI does
lychee --root-dir "$PWD/_book" --no-progress --offline --include-fragments '_book/**/*.html'
```

Each check exits non-zero on failure. Steps 2 and 4 also run in CI
(`.github/workflows/book.yml`), as does the `lychee` check.

## What to commit

After a re-run, review with `git status` and `git diff`, then commit:

- the rebuilt chapters under `content/`, and any images or data files copied
  next to them;
- `migration/report.md`, which lists every restored passage and edit;
- `_redirects`. It is generated: never edit it by hand, change
  `page-map.yml` and re-run `migrate.py`;
- the refreshed `_freeze/` results from step 3. A chapter with a stale or
  missing `_freeze/` entry is re-run on the CI runner.

## Adding a page to the map

`migrate.py` stops if an old page is missing from `page-map.yml` or listed
twice. Add the page under its chapter with `sources:`, then re-run the steps
above.
