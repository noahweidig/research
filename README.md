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
Workflows chain: Zotero sync -> Summarize -> Pages (each also runs manually).
- `scripts/summarize.py`: Anthropic API (`SUMMARY_MODEL`, default claude-sonnet-5-5). Skips papers whose input hash (prompt version + title + abstract + full text) matches the stored hash. Abstract-only papers are labeled. Bump `PROMPT_VERSION` to regenerate all.
- `scripts/synthesize.py`: rebuilds a page only when its paper set changed; updates send the existing page plus added/changed summaries only. Pages need >= 3 papers; first generation uses the 80 newest, the rest are added on later runs. Rejects output citing unknown keys.
- Site: Zensical (`zensical.toml`), Lucide `flask-conical` as logo and favicon. Index pages are generated at build time and not committed. Full texts are not published.

Extra setup: secret `ANTHROPIC_API_KEY`; Settings > Pages > Source: GitHub Actions. First run: dispatch Summarize with `limit` 20 to check output and cost.
Query the corpus: `grep -ril "prescribed" docs/summaries`, or read `docs/syntheses/`.
