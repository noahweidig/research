#!/usr/bin/env python3
"""Write one structured summary per paper to docs/summaries/<key>.md.

Skips papers whose input hash (prompt version + title + abstract + full text) matches the
stored hash, so existing summaries are never rewritten. Needs ANTHROPIC_API_KEY.
"""
import argparse, os, sys, time
from concurrent.futures import ThreadPoolExecutor
import kb

PROMPT_VERSION = "1"
MODEL = os.environ.get("SUMMARY_MODEL", "claude-sonnet-5-5")
MAX_FULL = 120_000
IDS = [t["id"] for t in kb.THEMES]
THEME_HELP = "\n".join(f"- {t['id']}: {t['scope']}" for t in kb.THEMES)
SYSTEM = f"""You summarize scientific papers on wildfire, ecology, and policy for a research knowledge base.
Use only the provided text. Never invent facts, numbers, or places. If something is not stated, write "Not stated".
If only an abstract is provided, say less; do not guess at methods beyond what the abstract says.
Be terse and concrete: include sample sizes, effect sizes, dates, and places when given.
themes: pick 0-3 ids from this list that the paper substantively informs:
{THEME_HELP}"""
TOOL = {
    "name": "record_summary",
    "description": "Record the structured summary.",
    "input_schema": {
        "type": "object",
        "properties": {
            "question": {"type": "string", "description": "Research question or objective, 1-2 sentences."},
            "methods": {"type": "string", "description": "Data, design, and analysis, 1-3 sentences."},
            "region": {"type": "string", "description": "Study region (US states/ecoregions if stated), or 'Not stated'."},
            "findings": {"type": "array", "items": {"type": "string"}, "description": "2-5 key findings, one sentence each."},
            "limitations": {"type": "array", "items": {"type": "string"}, "description": "Limitations stated or evident, 0-4 items."},
            "themes": {"type": "array", "items": {"type": "string", "enum": IDS}},
        },
        "required": ["question", "methods", "region", "findings", "limitations", "themes"],
    },
}


def clip(t):
    return t if len(t) <= MAX_FULL else t[: MAX_FULL - 20_000] + "\n\n[...]\n\n" + t[-20_000:]


def call_model(client, p):
    m = p["meta"]
    basis = "full text" if p["fulltext"] else "abstract only"
    body = clip(p["fulltext"]) if p["fulltext"] else p["abstract"]
    msg = f"Title: {m['title']}\nYear: {m.get('year')}\nJournal: {m.get('journal')}\nBasis: {basis}\n\n{body}"
    for i in range(4):
        try:
            r = client.messages.create(
                model=MODEL, max_tokens=1500, system=SYSTEM, tools=[TOOL],
                tool_choice={"type": "tool", "name": "record_summary"},
                messages=[{"role": "user", "content": msg}])
            return next(b.input for b in r.content if b.type == "tool_use")
        except Exception as e:
            print(f"  retry {i} {m['title'][:40]}: {e}", file=sys.stderr)
            time.sleep(2 ** (i + 1))
    return None


def bullets(xs):
    return "\n".join(f"- {x}" for x in xs) if xs else "Not stated"


def render(key, p, out, h):
    m = p["meta"]
    basis = "fulltext" if p["fulltext"] else "abstract"
    fm = dict(key=key, title=m["title"], authors=m.get("authors"), year=m.get("year"), doi=m.get("doi"),
              region=out["region"], themes=out["themes"], basis=basis, input_hash=h,
              prompt_version=PROMPT_VERSION, model=MODEL, paper=p["path"])
    repo = os.environ.get("GITHUB_REPOSITORY", "noahweidig/research")
    links = [f"[Full text file](https://github.com/{repo}/blob/main/{p['path']})"]
    if m.get("doi"):
        links.insert(0, f"[DOI](https://doi.org/{m['doi']})")
    note = ("" if basis == "fulltext" else
            '!!! warning "Abstract only"\n    No open-access full text was found. This summary is based on the abstract and may omit methods and limitations.\n\n')
    return (kb.dump_fm(fm) + f"\n# {m['title']}\n\n{kb.short_cite(m)} · {m.get('journal') or 'n.d.'} · "
            + " · ".join(links) + f"\n\n{note}## Question\n\n{out['question']}\n\n## Methods\n\n{out['methods']}\n\n"
            f"## Region\n\n{out['region']}\n\n## Findings\n\n{bullets(out['findings'])}\n\n"
            f"## Limitations\n\n{bullets(out['limitations'])}\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="max summaries to write (0 = all)")
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    import anthropic
    client = anthropic.Anthropic()
    papers, have = kb.load_papers(), kb.load_summaries()
    todo = []
    for key, p in papers.items():
        if not (p["fulltext"] or p["abstract"]):
            continue
        h = kb.sha(PROMPT_VERSION, p["meta"]["title"], p["abstract"], p["fulltext"])
        if key in have and have[key]["meta"].get("input_hash") == h:
            continue
        todo.append((key, p, h))
    for key in set(have) - set(papers):
        have[key]["path"].unlink()
        print("removed orphan", key, file=sys.stderr)
    if a.limit:
        todo = todo[: a.limit]
    print(f"{len(todo)} to summarize, {len(papers) - len(todo)} up to date/skipped", file=sys.stderr)
    kb.SUMMARIES.mkdir(parents=True, exist_ok=True)

    def work(t):
        key, p, h = t
        out = call_model(client, p)
        if out:
            (kb.SUMMARIES / f"{key}.md").write_text(render(key, p, out, h))
        return bool(out)

    with ThreadPoolExecutor(a.workers) as ex:
        ok = sum(ex.map(work, todo))
    print(f"wrote {ok}/{len(todo)}", file=sys.stderr)
    if todo and ok < len(todo):
        sys.exit(f"{len(todo) - ok} failed; rerun to retry")


if __name__ == "__main__":
    main()
