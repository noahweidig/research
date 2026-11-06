#!/usr/bin/env python3
"""Generate docs index pages at build time (not committed, so no git churn)."""
from collections import defaultdict
import kb

sums, syn = kb.load_summaries(), {}
for p in sorted(kb.SYNTHESES.glob("*.md")):
    if p.name != "index.md":
        fm, _ = kb.split_fm(p.read_text())
        syn[p.stem] = fm

lines = ["# Syntheses", "", "Living pages by theme. Each cites paper summaries and DOIs.", ""]
groups = defaultdict(list)
for k, fm in syn.items():
    groups[fm["group"]].append((fm["title"], k, len(fm["papers"])))
for g in sorted(groups):
    lines += [f"## {g}", ""] + [f"- [{t}]({k}.md) ({n} papers)" for t, k, n in sorted(groups[g])] + [""]
if not syn:
    lines.append("No syntheses yet.")
(kb.SYNTHESES / "index.md").write_text("\n".join(lines))

by_year = defaultdict(list)
for k, s in sums.items():
    by_year[str(s["meta"].get("year") or "n.d.")].append((s["meta"]["title"], k, kb.short_cite(s["meta"]), s["meta"]["basis"]))
lines = ["# Paper summaries", "", f"{len(sums)} summaries.", ""]
for y in sorted(by_year, reverse=True):
    lines += [f"## {y}", ""]
    lines += [f"- [{c}: {t}]({k}.md){' *(abstract only)*' if b == 'abstract' else ''}" for t, k, c, b in sorted(by_year[y])] + [""]
(kb.SUMMARIES / "index.md").write_text("\n".join(lines))
