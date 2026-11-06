# research
Claude's Knowledge Base for My Research


## Layout
- `papers/<topic>/<year>/<author>-<year>-<title>-<zkey>.md`: one file per Zotero item (YAML frontmatter + abstract + full text if open access)
- `papers/INDEX.md`, `papers/index.json`: generated indexes
- `config/topics.yml`: tag/title keywords -> topic folder
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
