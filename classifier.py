"""Filters items by card and tags them NEW / EXPIRING / DEVALUE."""
import re, json, hashlib, pathlib
from datetime import datetime, timedelta
from dateutil import parser as dateparser
from config import CARDS, KW_NEW, KW_EXPIRING, KW_DEVALUE, EXPIRING_WINDOW_DAYS

SEEN_FILE = pathlib.Path("seen.json")

def _hash(item):
    return hashlib.sha1((item["source"] + item["link"]).encode()).hexdigest()

def _matched_cards(text):
    t = text.lower()
    return [name for name, aliases in CARDS.items()
            if any(a in t for a in aliases)]

def _bucket(text):
    t = text.lower()
    buckets = []
    if any(k in t for k in KW_NEW):      buckets.append("NEW")
    if any(k in t for k in KW_EXPIRING): buckets.append("EXPIRING")
    if any(k in t for k in KW_DEVALUE):  buckets.append("DEVALUE")
    return buckets or ["UPDATE"]

def _expiring_soon(text):
    horizon = datetime.now() + timedelta(days=EXPIRING_WINDOW_DAYS)
    for m in re.finditer(r"(?:expires?|ends?|through|by|until)\s+"
                         r"([A-Za-z]+\s+\d{1,2}(?:,?\s+\d{4})?|\d{1,2}/\d{1,2}(?:/\d{2,4})?)",
                         text, flags=re.I):
        try:
            d = dateparser.parse(m.group(1), fuzzy=True)
            if datetime.now() <= d <= horizon:
                return d.date().isoformat()
        except Exception:
            pass
    return None

def classify(items):
    seen = json.loads(SEEN_FILE.read_text()) if SEEN_FILE.exists() else {}
    fresh = []
    for item in items:
        h = _hash(item)
        if h in seen:
            continue
        text = f"{item['title']} {item['summary']}"
        cards = _matched_cards(text)
        if not cards:
            continue
        buckets = _bucket(text)
        exp_date = _expiring_soon(text) if "EXPIRING" in buckets else None
        fresh.append({**item, "cards": cards, "buckets": buckets, "expires": exp_date})
        seen[h] = datetime.now().date().isoformat()
    cutoff = (datetime.now() - timedelta(days=90)).date().isoformat()
    seen = {k: v for k, v in seen.items() if v >= cutoff}
    SEEN_FILE.write_text(json.dumps(seen, indent=2))
    return fresh
