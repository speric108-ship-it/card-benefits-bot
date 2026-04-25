from feed_fetcher import fetch_all
from classifier   import classify
from notifier     import send

if __name__ == "__main__":
    raw   = fetch_all()
    fresh = classify(raw)
    send(fresh)
    print(f"Done. Fetched {len(raw)}, alerted on {len(fresh)}.")
