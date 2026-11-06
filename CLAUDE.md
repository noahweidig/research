# Knowledge base batches

Summaries batch: `python scripts/summaries.py todo --limit 50`; read `.batch/summaries.json` (follow its `instructions`); write `.batch/results.json`; run `python scripts/summaries.py write`; fix any SKIP lines; commit `docs/summaries`.
Syntheses: after summaries, `python scripts/syntheses.py todo`; read `.batch/syntheses.json`; write `.batch/synthesis/<theme>.md`; run `python scripts/syntheses.py write`; commit `docs/syntheses`.
Never hand-edit `papers/` (Zotero sync owns it). Use only paper text; no outside facts.
