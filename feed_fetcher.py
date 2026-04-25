"""Pulls RSS and Reddit JSON, returns a flat list of items."""
import time, requests, feedparser
from datetime import datetime, timezone
from config import RSS_FEEDS, REDDIT_FEEDS

UA = "biweekly-cc-bot/1.0 (personal use)"

def fetch_rss():
    items = []
    for source, url in RSS_FEEDS:
        try:
            d = feedparser.parse(url, request_headers={"User-Agent": UA})
            for e in d.entries:
                items.append({
                    "source": source,
                    "title":   e.get("title", ""),
                    "summary": e.get("summary", "")[:1500],
                    "link":    e.get("link", ""),
                    "published": e.get("published", ""),
                })
        except Exception as ex:
            print(f"[warn] {source}: {ex}")
    return items

def fetch_reddit():
    items = []
    for source, url in REDDIT_FEEDS:
        try:
            r = requests.get(url, headers={"User-Agent": UA}, timeout=20)
            r.raise_for_status()
            for child in r.json()["data"]["children"]:
                p = child["data"]
                items.append({
                    "source": source,
                    "title": p.get("title", ""),
                    "summary": p.get("selftext", "")[:1500],
                    "link":  "https://reddit.com" + p.get("permalink", ""),
                    "published": datetime.fromtimestamp(
                        p.get("created_utc", 0), tz=timezone.utc).isoformat(),
                })
            time.sleep(1)
        except Exception as ex:
            print(f"[warn] {source}: {ex}")
    return items

def fetch_all():
    return fetch_rss() + fetch_reddit()
