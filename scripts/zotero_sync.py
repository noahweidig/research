#!/usr/bin/env python3
"""Incremental Zotero -> markdown sync with open-access fulltext lookup."""
import argparse, json, os, re, sys, time, io
from pathlib import Path
import requests, yaml

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
STATE = ROOT / ".state" / "state.json"
TOPICS = yaml.safe_load((ROOT / "config" / "topics.yml").read_text())
UA = "research-kb/0.1 (mailto:{})"
S = requests.Session()
MIN_CHARS = 3000


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def get(url, retries=3, **kw):
    kw.setdefault("timeout", 60)
    for i in range(retries):
        try:
            r = S.get(url, **kw)
        except requests.RequestException as e:
            log("  net err", url, e); time.sleep(2 ** i); continue
        if r.status_code in (429, 503):
            time.sleep(int(r.headers.get("Retry-After", 2 ** (i + 1)))); continue
        return r
    return None


def zot_base():
    t = os.environ.get("ZOTERO_LIBRARY_TYPE", "user")
    return f"https://api.zotero.org/{t}s/{os.environ['ZOTERO_LIBRARY_ID']}"


def zot_headers():
    return {"Zotero-API-Key": os.environ["ZOTERO_API_KEY"], "Zotero-API-Version": "3"}


def zot_fetch_items(since):
    """Yield (items, library_version). Top-level + child attachments."""
    items, start, ver = [], 0, since
    while True:
        r = get(f"{zot_base()}/items", headers=zot_headers(),
                params={"since": since, "limit": 100, "start": start, "format": "json"})
        if r is None or r.status_code != 200:
            sys.exit(f"Zotero error: {r.status_code if r is not None else 'net'} {getattr(r, 'text', '')[:200]}")
        batch = r.json()
        ver = int(r.headers.get("Last-Modified-Version", ver))
        items += batch
        if len(batch) < 100:
            return items, ver
        start += 100


def zot_deleted(since):
    r = get(f"{zot_base()}/deleted", headers=zot_headers(), params={"since": since})
    return r.json().get("items", []) if r is not None and r.status_code == 200 else []


def slug(s, n=50):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n].strip("-") or "untitled"


def year_of(d):
    m = re.search(r"(19|20)\d\d", d or "")
    return m.group(0) if m else "undated"


def topic_of(tags, title):
    hay = [t.lower() for t in tags]
    for topic, kws in TOPICS.items():
        if any(k in t for t in hay for k in kws):
            return topic
    for topic, kws in TOPICS.items():
        if any(k in title.lower() for k in kws):
            return topic
    return "unsorted"


def authors_of(creators):
    out = []
    for c in creators:
        if c.get("creatorType") not in (None, "author"):
            continue
        out.append(c.get("name") or f"{c.get('lastName', '')}, {c.get('firstName', '')}".strip(", "))
    return out


# ---------- fulltext ----------
def pdf_to_md(data):
    import pymupdf4llm, pymupdf
    doc = pymupdf.open(stream=data, filetype="pdf")
    return pymupdf4llm.to_markdown(doc)


def html_to_md(html):
    from bs4 import BeautifulSoup
    from markdownify import markdownify
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
        t.decompose()
    node = soup.find("article") or soup.find("main") or soup.body or soup
    return markdownify(str(node), heading_style="ATX")


def fetch_url_md(url):
    r = get(url, headers={"User-Agent": UA.format(os.environ.get("UNPAYWALL_EMAIL", ""))})
    if r is None or r.status_code != 200:
        return None
    ct = r.headers.get("Content-Type", "").lower()
    if "pdf" in ct or r.content[:5] == b"%PDF-":
        return pdf_to_md(r.content)
    if "html" in ct:
        return html_to_md(r.text)
    return None


def src_unpaywall(doi):
    r = get(f"https://api.unpaywall.org/v2/{doi}", params={"email": os.environ["UNPAYWALL_EMAIL"]})
    if r is None or r.status_code != 200:
        return []
    j = r.json()
    urls = []
    for loc in ([j.get("best_oa_location")] if j.get("best_oa_location") else []) + j.get("oa_locations", []):
        for k in ("url_for_pdf", "url"):
            if loc.get(k) and loc[k] not in [u for u, _ in urls]:
                urls.append((loc[k], "unpaywall"))
    return urls


def src_europepmc(doi):
    r = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search",
            params={"query": f'DOI:"{doi}"', "format": "json", "resultType": "lite"})
    if r is None or r.status_code != 200:
        return []
    for res in r.json().get("resultList", {}).get("result", []):
        if res.get("pmcid") and res.get("isOpenAccess") == "Y":
            return [(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{res['pmcid']}/fullTextXML", "europepmc")]
    return []


def src_s2(doi):
    r = get(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
            params={"fields": "openAccessPdf,externalIds"})
    if r is None or r.status_code != 200:
        return []
    j = r.json()
    out = []
    if (j.get("openAccessPdf") or {}).get("url"):
        out.append((j["openAccessPdf"]["url"], "semanticscholar"))
    ax = (j.get("externalIds") or {}).get("ArXiv")
    if ax:
        out.append((f"https://arxiv.org/pdf/{ax}", "arxiv"))
    return out


def jats_to_md(xml):
    from bs4 import BeautifulSoup
    s = BeautifulSoup(xml, "xml")
    out = []
    for sec in s.find_all(["abstract", "body"]):
        for el in sec.find_all(["title", "p"]):
            if el.name == "title":
                out.append(f"\n## {el.get_text(' ', strip=True)}\n")
            elif not el.find_parent("table-wrap"):
                out.append(el.get_text(" ", strip=True) + "\n")
    return "\n".join(out)


def get_fulltext(meta):
    """Return (markdown|None, source|None, license_note)."""
    doi = meta["doi"]
    cands = []
    if doi:
        if os.environ.get("UNPAYWALL_EMAIL"):
            cands += src_unpaywall(doi)
        cands += src_europepmc(doi) + src_s2(doi)
    m = re.search(r"arxiv\.org/(?:abs|pdf)/([\w./-]+)", meta.get("url", ""))
    if m:
        cands.append((f"https://arxiv.org/pdf/{m.group(1)}", "arxiv"))
    seen = set()
    for url, src in cands:
        if url in seen:
            continue
        seen.add(url)
        try:
            if src == "europepmc":
                r = get(url)
                md = jats_to_md(r.text) if r is not None and r.status_code == 200 else None
            else:
                md = fetch_url_md(url)
        except Exception as e:
            log("  convert err", url, e); continue
        if md and len(md) >= MIN_CHARS:
            return md, f"{src}: {url}"
    return None, None


# ---------- main ----------
def render(meta, body):
    fm = {k: v for k, v in meta.items() if not k.startswith("_")}
    head = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000)
    abstract = f"## Abstract\n\n{meta['_abstract']}\n\n" if meta.get("_abstract") else ""
    full = f"## Full text\n\n{body}\n" if body else ""
    return f"---\n{head}---\n\n# {meta['title']}\n\n{abstract}{full}"


def build_index(state):
    rows = {}
    for p in sorted(PAPERS.rglob("*.md")):
        if p.name == "INDEX.md":
            continue
        txt = p.read_text()
        m = re.match(r"---\n(.*?)\n---", txt, re.S)
        if not m:
            continue
        fm = yaml.safe_load(m.group(1))
        rows.setdefault(p.parts[len(PAPERS.parts)], []).append((p, fm))
    lines = ["# Paper index", "", f"Total: {sum(len(v) for v in rows.values())}", ""]
    for topic in sorted(rows):
        lines += [f"## {topic} ({len(rows[topic])})", "", "| Year | Title | Journal | Fulltext |", "|---|---|---|---|"]
        for p, fm in sorted(rows[topic], key=lambda x: (str(x[1].get("year")), x[1].get("title", ""))):
            rel = p.relative_to(PAPERS).as_posix()
            t = str(fm.get("title", "")).replace("|", "/")
            lines.append(f"| {fm.get('year')} | [{t}]({rel}) | {str(fm.get('journal') or '').replace('|', '/')} | {fm.get('fulltext_status')} |")
        lines.append("")
    (PAPERS / "INDEX.md").write_text("\n".join(lines))
    (PAPERS / "index.json").write_text(json.dumps(
        [dict(fm, path=p.relative_to(PAPERS).as_posix()) for v in rows.values() for p, fm in v],
        indent=1, default=str))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true", help="ignore stored version, refetch all")
    ap.add_argument("--limit", type=int, help="max items to process (testing)")
    ap.add_argument("--retry-missing", action="store_true", help="retry fulltext for metadata-only items")
    ap.add_argument("--no-fulltext", action="store_true")
    a = ap.parse_args()
    for k in ("ZOTERO_API_KEY", "ZOTERO_LIBRARY_ID"):
        if not os.environ.get(k):
            sys.exit(f"missing env {k}")
    if not os.environ.get("UNPAYWALL_EMAIL"):
        log("warn: UNPAYWALL_EMAIL unset; Unpaywall skipped")
    PAPERS.mkdir(exist_ok=True)
    state = json.loads(STATE.read_text()) if STATE.exists() else {"version": 0, "items": {}}
    since = 0 if a.full else state["version"]
    items, new_ver = zot_fetch_items(since)
    log(f"{len(items)} changed items since v{since}")
    top = {i["key"]: i for i in items if i["data"]["itemType"] not in ("attachment", "note", "annotation")}
    if a.retry_missing:
        for k, v in state["items"].items():
            if v["status"] == "metadata-only" and k not in top:
                r = get(f"{zot_base()}/items/{k}", headers=zot_headers())
                if r is not None and r.status_code == 200:
                    top[k] = r.json()
    for k in zot_deleted(since) if since else []:
        old = state["items"].pop(k, None)
        if old and (ROOT / old["path"]).exists():
            (ROOT / old["path"]).unlink()
    n = 0
    for key, it in top.items():
        if a.limit and n >= a.limit:
            break
        n += 1
        d = it["data"]
        title = d.get("title") or "Untitled"
        tags = [t["tag"] for t in d.get("tags", [])]
        authors = authors_of(d.get("creators", []))
        year = year_of(d.get("date"))
        topic = topic_of(tags, title)
        first = slug(authors[0].split(",")[0], 20) if authors else "anon"
        rel = f"papers/{topic}/{year}/{first}-{year}-{slug(title, 40)}-{key.lower()}.md"
        doi = (d.get("DOI") or "").strip() or None
        prev = state["items"].get(key)
        meta = {
            "title": title, "authors": authors, "year": year if year != "undated" else None,
            "journal": d.get("publicationTitle") or d.get("proceedingsTitle") or d.get("repository") or None,
            "doi": doi, "tags": tags, "zotero_key": key, "item_type": d["itemType"],
            "url": d.get("url") or (f"https://doi.org/{doi}" if doi else None),
            "source_url": None, "fulltext_status": "metadata-only",
            "synced": time.strftime("%Y-%m-%d"),
            "_abstract": d.get("abstractNote"),
        }
        body = None
        if prev and prev["status"] == "fulltext" and not a.full and (ROOT / prev["path"]).exists():
            old = (ROOT / prev["path"]).read_text()
            body = old.split("## Full text\n\n", 1)[1].rstrip("\n") if "## Full text\n\n" in old else None
            meta["source_url"] = prev.get("source")
            meta["fulltext_status"] = "fulltext" if body else "metadata-only"
        elif not a.no_fulltext:
            log(f"[{n}] fulltext: {title[:70]}")
            body, src = get_fulltext(meta)
            if body:
                meta["fulltext_status"], meta["source_url"] = "fulltext", src
        if prev and prev["path"] != rel and (ROOT / prev["path"]).exists():
            (ROOT / prev["path"]).unlink()
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(meta, body))
        state["items"][key] = {"path": rel, "status": meta["fulltext_status"], "source": meta["source_url"]}
    if not a.limit:
        state["version"] = new_ver
    STATE.write_text(json.dumps(state, indent=1, sort_keys=True))
    for d in sorted(PAPERS.rglob("*"), reverse=True):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    build_index(state)
    log("done")


if __name__ == "__main__":
    main()
