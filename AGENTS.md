# Notes for agents working on this repository

Environmental Computing is a Quarto book of R tutorials, published at environmentalcomputing.net. Contributor conventions (layout, naming, where images and data go, building, caching) are in [content/contributing.qmd](content/contributing.qmd); read it before adding or moving pages.

## Deployment

See "How the site is deployed" in [README.qmd](README.qmd) for the full picture. In short: GitHub Actions ([.github/workflows/book.yml](.github/workflows/book.yml)) renders the book and uploads `_book/` to Netlify; pushes to `master` go live, pull requests get deploy previews. The Netlify site belongs to Daniel Falster's (dfalster) Netlify account; only he can create tokens or change site settings.

Rules that are easy to break without noticing:

- **Keep `ignore = "exit 0"` in `netlify.toml`.** Netlify's build image cannot run R. If Netlify tries to build the site itself, those builds fail or race with the Actions deploy.
- **Deploys depend on the `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID` repository secrets.** Never remove or rename them, and never weaken the "Check Netlify credentials" step: without it, a missing secret makes the deploy skip without failing, and the live site stops updating without anyone noticing (this happened for months under the old Hugo site). Secrets are set by a human; ask rather than work around a missing one.
- **Commit `_freeze/`.** CI re-runs only the chapters whose source changed, using the committed frozen results. A chapter whose `_freeze/` entry is missing or stale is re-executed on the runner.
- **Keep `_redirects` in step with the chapters.** It maps old Hugo and WordPress addresses (linked from course materials) to book chapters and sections, and is copied into `_book/` through `resources` in `_quarto.yml`. When you move or rename a chapter, or change a heading a redirect points to, update the matching lines; CI's "Check redirects" step fails otherwise. Never delete redirects.
- **Edit chapters directly.** The `.qmd` files are the source. `migration/` is a record of the 2026 port from Hugo; don't re-run `migrate.py` (it refuses without `--force`) or record edits in `page-map.yml`.
- **Edit `README.qmd`, not only `README.md`.** `README.md` is rendered from it (`quarto render README.qmd`, which needs R and the GitHub API); if you change one by hand, make the same change to the other.

## Cross-repo context (maintainers)

This book is a shared resource for UNSW's BEES quantitative-skills subjects, which link to its chapters as reading. Conventions that span those repos (labels, `[prefix]` issue titles, the project board, cross-repo playbooks) live in the hub, `nicercode/UNSW_BEES_quantitative_curriculum`. The hub is **private**: it needs nicercode access, and its content must not be copied into this public repo. Guidance for outside contributors stays here, in [content/contributing.qmd](content/contributing.qmd).

Two rules follow from this book's place in the family:

- Course materials link to chapters by URL, so the `_redirects` rule above protects every subject, not only this site.
- Nothing from a subject's assessments (solutions, answer keys, exam questions) or any student data belongs in this repo, even as an example.
