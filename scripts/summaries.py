#!/usr/bin/env python3
"""Batch workflow for per-paper summaries, written by a Claude session (no API key).

  python scripts/summaries.py todo [--limit 50]   -> .batch/summaries.json (papers needing a summary)
  python scripts/summaries.py write                -> validates .batch/results.json, writes docs/summaries/<key>.md

results.json: {"<KEY>": {"question": str, "methods": str, "region": str,
  "findings": [str], "limitations": [str], "themes": [theme ids]}}
Unchanged papers (same input hash) are never listed or rewritten.
"""
import argparse, json, os, sys
import kb

PROMPT_VERSION = "1"
MAX_FULL = 100_000
BATCH = kb.ROOT / ".batch"
IDS = {t["id"] for t in kb.THEMES}
REQ = {"question": str, "methods": str, "region": str, "findings": list, "limitations": list, "themes": list}
INSTR = ("For each paper write a summary using ONLY its text. Never invent facts, numbers, or places; write 'Not stated' "
         "when absent. basis=abstract: say less, do not guess methods. Be terse and concrete (sample sizes, effects, dates, places). "
         "findings: 2-5 one-sentence items. limitations: 0-4. themes: 0-3 ids from the 'themes' list. "
         "Save {KEY: {question, methods, region, findings, limitations, themes}} to .batch/results.json, then run `write`.")


def clip(t):
    return t if len(t) <= MAX_FULL else t[: MAX_FULL - 15_000] + "\n\n[...]\n\n" + t[-15_000:]


def input_hash(p):
    return kb.sha(PROMPT_VERSION, p["meta"]["title"], p["abstract"], p["fulltext"])


def cmd_todo(a):
    have = kb.load_summaries()
    papers = kb.load_papers()
    for key in set(have) - set(papers):
        have[key]["path"].unlink()
        print("removed orphan summary", key)
    todo = []
    for key, p in papers.items():
        if not (p["fulltext"] or p["abstract"]):
            continue
        h = input_hash(p)
        if key in have and have[key]["meta"].get("input_hash") == h:
            continue
        m = p["meta"]
        todo.append(dict(key=key, hash=h, basis="fulltext" if p["fulltext"] else "abstract",
                         title=m["title"], authors=m.get("authors"), year=m.get("year"), journal=m.get("journal"),
                         text=clip(p["fulltext"]) if p["fulltext"] else p["abstract"]))
    total = len(todo)
    todo = todo[: a.limit] if a.limit else todo
    BATCH.mkdir(exist_ok=True)
    (BATCH / "summaries.json").write_text(json.dumps(
        dict(instructions=INSTR, themes={t["id"]: t["scope"] for t in kb.THEMES}, papers=todo), indent=1))
    print(f"{len(todo)} in batch ({total} pending total) -> .batch/summaries.json")


def bullets(xs):
    return "\n".join(f"- {x}" for x in xs) if xs else "Not stated"


def render(item, p, out):
    m = p["meta"]
    fm = dict(key=item["key"], title=m["title"], authors=m.get("authors"), year=m.get("year"), doi=m.get("doi"),
              region=out["region"], themes=out["themes"], basis=item["basis"], input_hash=item["hash"],
              prompt_version=PROMPT_VERSION, paper=p["path"])
    repo = os.environ.get("GITHUB_REPOSITORY", "noahweidig/research")
    links = [f"[Full text file](https://github.com/{repo}/blob/main/{p['path']})"]
    if m.get("doi"):
        links.insert(0, f"[DOI](https://doi.org/{m['doi']})")
    note = ("" if item["basis"] == "fulltext" else
            '!!! warning "Abstract only"\n    No open-access full text was found. This summary is based on the abstract and may omit methods and limitations.\n\n')
    return (kb.dump_fm(fm) + f"\n# {m['title']}\n\n{kb.short_cite(m)} · {m.get('journal') or 'n.d.'} · " + " · ".join(links)
            + f"\n\n{note}## Question\n\n{out['question']}\n\n## Methods\n\n{out['methods']}\n\n## Region\n\n{out['region']}\n\n"
            f"## Findings\n\n{bullets(out['findings'])}\n\n## Limitations\n\n{bullets(out['limitations'])}\n")


def check(out):
    for k, t in REQ.items():
        if not isinstance(out.get(k), t) or (t is str and not out[k].strip()):
            return f"bad field {k}"
    if not out["findings"]:
        return "no findings"
    if any(not isinstance(x, str) for x in out["findings"] + out["limitations"] + out["themes"]):
        return "non-string list item"
    if set(out["themes"]) - IDS:
        return f"unknown themes {sorted(set(out['themes']) - IDS)}"
    return None


def cmd_write(a):
    batch = {i["key"]: i for i in json.loads((BATCH / "summaries.json").read_text())["papers"]}
    results = json.loads((BATCH / "results.json").read_text())
    papers = kb.load_papers()
    kb.SUMMARIES.mkdir(parents=True, exist_ok=True)
    ok = bad = 0
    for key, out in results.items():
        item, p = batch.get(key), papers.get(key)
        err = ("not in batch" if not item else "paper missing" if not p else
               "paper changed since batch; rerun todo" if input_hash(p) != item["hash"] else check(out))
        if err:
            print(f"SKIP {key}: {err}", file=sys.stderr)
            bad += 1
            continue
        (kb.SUMMARIES / f"{key}.md").write_text(render(item, p, out))
        ok += 1
    print(f"wrote {ok}, rejected {bad}, not in results {len(set(batch) - set(results))}")
    if bad:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("todo").add_argument("--limit", type=int, default=50)
    sp.add_parser("write")
    a = ap.parse_args()
    {"todo": cmd_todo, "write": cmd_write}[a.cmd](a)


if __name__ == "__main__":
    main()
