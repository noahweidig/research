#!/usr/bin/env python3
"""Write/update living synthesis pages docs/syntheses/<theme>.md from paper summaries.

A page is regenerated only when its paper set (key -> summary hash) changed. Updates send
the existing page plus only the added/changed summaries. Needs ANTHROPIC_API_KEY.
"""
import argparse, os, re, sys
import yaml
import kb

MODEL = os.environ.get("SYNTH_MODEL", "claude-sonnet-5-5")
CFG = yaml.safe_load((kb.ROOT / "config" / "themes.yml").read_text())
SYSTEM = """You maintain a living literature synthesis page for a wildfire, ecology, and US policy knowledge base.
Rules:
- Use ONLY the provided paper summaries. No outside facts.
- Cite every claim inline as [Smith et al. 2020](../summaries/KEY.md) using the exact KEY provided. Never cite a key not provided.
- Flag claims resting only on abstract-only papers with "(abstract only)".
- State disagreements and gaps explicitly. Note US regions where evidence is thin.
- Target 500-900 words. Markdown only, no title line, no References section (added automatically).
- Sections: ## Overview, ## Key findings (grouped bullets), ## Disagreements and gaps, ## US regional notes.
- When updating, revise the existing page: fold in new papers, drop papers listed as removed, keep structure and length."""


def paper_block(key, s):
    m, b = s["meta"], s["body"]
    return (f"### KEY={key} | {kb.short_cite(m)} | basis={m['basis']} | region={m.get('region')}\n"
            f"{m['title']}\nQuestion: {kb.section(b, 'Question')}\nFindings:\n{kb.section(b, 'Findings')}\n"
            f"Limitations:\n{kb.section(b, 'Limitations')}\n")


def generate(client, theme, existing, add, removed, sums):
    head = f"Theme: {theme['title']}\nScope: {theme['scope']}\n\n"
    if existing:
        head += f"EXISTING PAGE:\n{existing}\n\nREMOVED KEYS: {', '.join(removed) or 'none'}\n\nNEW OR CHANGED PAPERS:\n"
    else:
        head += "Write the page from these papers:\n"
    msg = head + "\n".join(paper_block(k, sums[k]) for k in add)
    r = client.messages.create(model=MODEL, max_tokens=3000, system=SYSTEM,
                               messages=[{"role": "user", "content": msg}])
    return "".join(b.text for b in r.content if b.type == "text").strip()


def references(keys, sums):
    rows = []
    for k in sorted(keys, key=lambda k: kb.short_cite(sums[k]["meta"])):
        m = sums[k]["meta"]
        doi = f" [doi:{m['doi']}](https://doi.org/{m['doi']})" if m.get("doi") else ""
        tag = " *(abstract only)*" if m["basis"] == "abstract" else ""
        rows.append(f"- [{kb.short_cite(m)}](../summaries/{k}.md): {m['title']}.{doi}{tag}")
    return "\n".join(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="theme id")
    a = ap.parse_args()
    import anthropic
    client = anthropic.Anthropic()
    sums = kb.load_summaries()
    kb.SYNTHESES.mkdir(parents=True, exist_ok=True)
    for t in CFG["themes"]:
        if a.only and t["id"] != a.only:
            continue
        keys = {k: s["meta"]["input_hash"] for k, s in sums.items() if t["id"] in (s["meta"].get("themes") or [])}
        page = kb.SYNTHESES / f"{t['id']}.md"
        old_fm, old_body = kb.split_fm(page.read_text()) if page.exists() else ({}, "")
        prev = old_fm.get("papers") or {}
        if len(keys) < CFG["min_papers"] and not prev:
            continue
        added = [k for k in keys if prev.get(k) != keys[k]]
        removed = [k for k in prev if k not in keys]
        if not added and not removed:
            continue
        year = lambda k: str(sums[k]["meta"].get("year") or "")
        added.sort(key=year, reverse=True)
        added = added[: CFG["max_papers"]]
        included = {k: h for k, h in keys.items() if k in prev or k in added}
        included = {k: h for k, h in included.items() if k in keys}
        print(f"{t['id']}: +{len(added)} -{len(removed)} ({len(keys) - len(included)} pending)", file=sys.stderr)
        body_only = re.split(r"\n## References\n", old_body)[0].strip() if old_body else ""
        body_only = re.sub(r"^# .*\n+", "", body_only)
        text = generate(client, t, body_only, added, removed, sums)
        bad = set(re.findall(r"\(\.\./summaries/([A-Za-z0-9]+)\.md\)", text)) - set(included)
        if bad:
            print(f"  skip {t['id']}: cites unknown keys {sorted(bad)}", file=sys.stderr)
            continue
        fm = dict(theme=t["id"], group=t["group"], title=t["title"], model=MODEL, papers=dict(sorted(included.items())))
        page.write_text(kb.dump_fm(fm) + f"\n# {t['title']}\n\n{text}\n\n## References\n\n{references(included, sums)}\n")


if __name__ == "__main__":
    main()
