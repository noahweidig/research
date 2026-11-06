#!/usr/bin/env python3
"""Batch workflow for living synthesis pages, written by a Claude session (no API key).

  python scripts/syntheses.py todo [--only ID]  -> .batch/syntheses.json (stale themes + new/changed summaries)
  python scripts/syntheses.py write             -> validates .batch/synthesis/<id>.md, writes docs/syntheses/<id>.md

A theme is stale when its paper set (key -> summary hash) differs from the page's stored set. The session
writes only the page body (no title, no References); code adds frontmatter and the DOI reference list.
"""
import argparse, json, re, sys
import yaml
import kb

BATCH = kb.ROOT / ".batch"
CFG = yaml.safe_load((kb.ROOT / "config" / "themes.yml").read_text())
INSTR = ("Per theme, write/update the page body markdown using ONLY the given summaries, no outside facts. Cite every claim "
         "inline as [Smith et al. 2020](../summaries/KEY.md) with exact KEYs. Mark claims resting only on basis=abstract "
         "papers '(abstract only)'. State disagreements, gaps, thin US regions. 500-900 words. Sections: ## Overview, "
         "## Key findings (grouped bullets), ## Disagreements and gaps, ## US regional notes. No title line, no References. "
         "If 'existing' is non-empty, revise it: add 'add' papers, drop 'removed' keys, keep structure and length. "
         "Save to .batch/synthesis/<theme id>.md, then run `write`.")


def block(key, s):
    m, b = s["meta"], s["body"]
    return dict(key=key, cite=kb.short_cite(m), basis=m["basis"], region=m.get("region"), title=m["title"],
                question=kb.section(b, "Question"), findings=kb.section(b, "Findings"),
                limitations=kb.section(b, "Limitations"))


def plan(sums, only=None):
    out = []
    for t in CFG["themes"]:
        if only and t["id"] != only:
            continue
        keys = {k: s["meta"]["input_hash"] for k, s in sums.items() if t["id"] in (s["meta"].get("themes") or [])}
        page = kb.SYNTHESES / f"{t['id']}.md"
        fm, body = kb.split_fm(page.read_text()) if page.exists() else ({}, "")
        prev = fm.get("papers") or {}
        if len(keys) < CFG["min_papers"] and not prev:
            continue
        add = sorted((k for k in keys if prev.get(k) != keys[k]),
                     key=lambda k: str(sums[k]["meta"].get("year") or ""), reverse=True)[: CFG["max_papers"]]
        removed = [k for k in prev if k not in keys]
        if not add and not removed:
            continue
        included = {k: h for k, h in keys.items() if k in prev or k in add}
        existing = re.sub(r"^# .*\n+", "", re.split(r"\n## References\n", body)[0].strip()) if body else ""
        out.append(dict(theme=t, existing=existing, add=[block(k, sums[k]) for k in add], removed=removed,
                        pending=len(keys) - len(included), papers=included))
    return out


def references(keys, sums):
    rows = []
    for k in sorted(keys, key=lambda k: kb.short_cite(sums[k]["meta"])):
        m = sums[k]["meta"]
        doi = f" [doi:{m['doi']}](https://doi.org/{m['doi']})" if m.get("doi") else ""
        tag = " *(abstract only)*" if m["basis"] == "abstract" else ""
        rows.append(f"- [{kb.short_cite(m)}](../summaries/{k}.md): {m['title']}.{doi}{tag}")
    return "\n".join(rows)


def cmd_todo(a):
    stale = plan(kb.load_summaries(), a.only)
    BATCH.mkdir(exist_ok=True)
    (BATCH / "synthesis").mkdir(exist_ok=True)
    (BATCH / "syntheses.json").write_text(json.dumps(dict(instructions=INSTR, themes=stale), indent=1))
    for s in stale:
        print(f"{s['theme']['id']}: +{len(s['add'])} -{len(s['removed'])} ({s['pending']} pending)")
    print(f"{len(stale)} stale -> .batch/syntheses.json")


def cmd_write(a):
    sums = kb.load_summaries()
    stale = {s["theme"]["id"]: s for s in json.loads((BATCH / "syntheses.json").read_text())["themes"]}
    bad = 0
    for tid, s in stale.items():
        f = BATCH / "synthesis" / f"{tid}.md"
        if not f.exists():
            continue
        text = f.read_text().strip()
        cited = set(re.findall(r"\(\.\./summaries/([A-Za-z0-9]+)\.md\)", text))
        fails = [] if cited else ["no citations"]
        if cited - set(s["papers"]):
            fails.append(f"unknown keys {sorted(cited - set(s['papers']))}")
        if re.search(r"^# |^## References", text, re.M):
            fails.append("has title/References")
        if set(s["papers"]) - set(sums):
            fails.append("summary removed since batch")
        if fails:
            print(f"SKIP {tid}: {'; '.join(fails)}", file=sys.stderr)
            bad += 1
            continue
        t = s["theme"]
        fm = dict(theme=tid, group=t["group"], title=t["title"], papers=dict(sorted(s["papers"].items())))
        kb.SYNTHESES.mkdir(parents=True, exist_ok=True)
        (kb.SYNTHESES / f"{tid}.md").write_text(
            kb.dump_fm(fm) + f"\n# {t['title']}\n\n{text}\n\n## References\n\n{references(s['papers'], sums)}\n")
        print("wrote", tid)
    if bad:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("todo").add_argument("--only")
    sp.add_parser("write")
    a = ap.parse_args()
    {"todo": cmd_todo, "write": cmd_write}[a.cmd](a)


if __name__ == "__main__":
    main()
