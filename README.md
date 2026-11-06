# research
Claude's Knowledge Base for My Research


## Layout
- `papers/<topic>/<year>/<author>-<year>-<title>-<zkey>.md`: one file per Zotero item (YAML frontmatter + abstract + full text if open access)
- `papers/INDEX.md`, `papers/index.json`: generated indexes
- `config/topics.yml`: tag/title keywords -> topic folder
- `docs/summaries/<zkey>.md`: one structured summary per paper (question, methods, region, findings, limitations, themes). Separate from the paper file; written once, rewritten only if the paper's text changes
- `docs/syntheses/<theme>.md`: living topic pages with inline citations + DOI reference lists
- `config/themes.yml`: synthesis themes (add/edit to change pages)
- `.state/state.json`: Zotero library version + item->path map (enables incremental sync)

## Setup
Repo secrets: `ZOTERO_API_KEY`, `ZOTERO_LIBRARY_ID`, `UNPAYWALL_EMAIL`.
Repo variables (optional): `ZOTERO_LIBRARY_TYPE` (`user` default, or `group`).

## Run
```
pip install -r requirements.txt
python scripts/zotero_sync.py [--full] [--retry-missing] [--limit N]
```
Action runs Mondays 09:00 UTC and on manual dispatch.

## Fulltext sources (in order)
DOI lookup: Unpaywall, Europe PMC (OA), Semantic Scholar openAccessPdf, arXiv. No paywalled scraping. Items with nothing usable stay `fulltext_status: metadata-only`; converted text under 3000 chars is rejected.

## Summaries, syntheses, site
No Anthropic API key needed. A Claude session (your subscription) writes summaries and syntheses in batches; scripts handle listing, validation, and writing.
- Summaries: `python scripts/summaries.py todo --limit 50` writes `.batch/summaries.json` (new or changed papers only; unchanged hash = skipped, never rewritten). The session writes `.batch/results.json`, then `python scripts/summaries.py write` validates (schema, theme ids, paper unchanged) and writes `docs/summaries/<zkey>.md`. Abstract-only papers are labeled. Bump `PROMPT_VERSION` to regenerate all.
- Syntheses: `python scripts/syntheses.py todo` lists stale themes (paper set changed) with existing page + new/changed summaries. The session writes `.batch/synthesis/<theme>.md` bodies, then `python scripts/syntheses.py write` validates citations and adds frontmatter and the DOI reference list. Themes need >= 3 papers; first pass uses the 80 newest, the rest follow on later runs.
- Site: Zensical (`zensical.toml`), Lucide `flask-conical` as logo and favicon. Index pages are generated at build time and not committed. Full texts are not published. `Pages` workflow deploys on pushes to main that touch the site.

Setup: Settings > Pages > Source: GitHub Actions.

Kick off a batch: tell a Claude session "run the next summary batch" (repeat until 0 pending), then "update the syntheses". Instructions for sessions are in `CLAUDE.md`. Commit `docs/summaries` and `docs/syntheses` to a branch/PR.

Query the corpus: `grep -ril "prescribed" docs/summaries`, or read `docs/syntheses/`.

Optional later automation: the Claude Code GitHub Action with `CLAUDE_CODE_OAUTH_TOKEN` (create via `claude setup-token`, add as a repo secret) could run the same batch prompt on a schedule. Not required, not set up here.
