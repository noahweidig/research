"""Shared helpers: read papers, summaries, themes."""
import hashlib, re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
SUMMARIES = ROOT / "docs" / "summaries"
SYNTHESES = ROOT / "docs" / "syntheses"
THEMES = yaml.safe_load((ROOT / "config" / "themes.yml").read_text())["themes"]
FM = re.compile(r"\A---\n(.*?)\n---\n?(.*)", re.S)


def split_fm(txt):
    m = FM.match(txt)
    return (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, txt)


def dump_fm(fm):
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000) + "---\n"


def section(body, name):
    m = re.search(rf"^## {name}\n\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""


def load_papers():
    """key -> dict(meta, abstract, fulltext, path, hash)."""
    out = {}
    for p in sorted(PAPERS.rglob("*.md")):
        if p.name == "INDEX.md":
            continue
        fm, body = split_fm(p.read_text())
        key = fm.get("zotero_key")
        if not key:
            continue
        abstract, full = section(body, "Abstract"), section(body, "Full text")
        out[key] = dict(meta=fm, abstract=abstract, fulltext=full,
                        path=p.relative_to(ROOT).as_posix())
    return out


def load_summaries():
    out = {}
    for p in sorted(SUMMARIES.glob("*.md")):
        if p.name == "index.md":
            continue
        fm, body = split_fm(p.read_text())
        if fm.get("key"):
            out[fm["key"]] = dict(meta=fm, body=body, path=p)
    return out


def short_cite(meta):
    a = meta.get("authors") or []
    last = a[0].split(",")[0] if a else "Anon"
    et = " et al." if len(a) > 2 else (f" & {a[1].split(',')[0]}" if len(a) == 2 else "")
    return f"{last}{et} {meta.get('year') or 'n.d.'}"


def sha(*parts):
    h = hashlib.sha256()
    for p in parts:
        h.update(str(p).encode())
        h.update(b"\0")
    return h.hexdigest()[:16]
