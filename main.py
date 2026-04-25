from feed_fetcher import fetch_all
from classifier   import classify
from summarizer   import summarize
import os, requests

if __name__ == "__main__":
    raw   = fetch_all()
    fresh = classify(raw)
    print(f"Fetched {len(raw)}, matched {len(fresh)}.")

    summary = summarize(fresh)
    print(summary)

    token  = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
    target = os.environ["LINE_TARGET_ID"]

    for chunk in [summary[i:i+4900] for i in range(0, len(summary), 4900)]:
        r = requests.post("https://api.line.me/v2/bot/message/push",
            headers={"Authorization": f"Bearer {token}",
                     "Content-Type": "application/json"},
            json={"to": target, "messages":[{"type":"text","text": chunk}]},
            timeout=15)
        r.raise_for_status()

    print("Done. Message sent to LINE.")
    
