"""Formats the digest and sends it to Discord (or LINE)."""
import os, requests, json
from config import NOTIFIER, CARDS

def _format(items):
    if not items:
        return "🟢 Biweekly card check — no new updates this cycle."
    by_bucket = {"NEW": [], "EXPIRING": [], "DEVALUE": [], "UPDATE": []}
    for it in items:
        priority = next(b for b in ("EXPIRING","DEVALUE","NEW","UPDATE")
                          if b in it["buckets"])
        by_bucket[priority].append(it)
    icons = {"NEW":"🆕","EXPIRING":"⏰","DEVALUE":"⚠️","UPDATE":"📝"}
    titles = {"NEW":"New benefits / offers","EXPIRING":"Expiring soon — use ASAP",
              "DEVALUE":"Cancellations / devaluations","UPDATE":"Other updates"}
    lines = ["📬 Biweekly credit-card benefits digest", ""]
    for b in ("EXPIRING","DEVALUE","NEW","UPDATE"):
        if not by_bucket[b]: continue
        lines.append(f"{icons[b]} {titles[b]}")
        for it in by_bucket[b]:
            tag = ", ".join(it["cards"])
            extra = f" — expires {it['expires']}" if it["expires"] else ""
            lines.append(f"• {it['title']} — {tag} ({it['source']}){extra}")
            lines.append(f"  {it['link']}")
        lines.append("")
    return "\n".join(lines)

def send_discord(text):
    url = os.environ["DISCORD_WEBHOOK_URL"]
    for chunk in [text[i:i+1900] for i in range(0, len(text), 1900)]:
        r = requests.post(url, json={"content": chunk}, timeout=15)
        r.raise_for_status()

def send_line(text):
    token = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
    target = os.environ["LINE_TARGET_ID"]
    for chunk in [text[i:i+4900] for i in range(0, len(text), 4900)]:
        r = requests.post("https://api.line.me/v2/bot/message/push",
            headers={"Authorization": f"Bearer {token}",
                     "Content-Type": "application/json"},
            json={"to": target, "messages":[{"type":"text","text": chunk}]},
            timeout=15)
        r.raise_for_status()

def send(items):
    text = _format(items)
    print(text)
    (send_discord if NOTIFIER == "discord" else send_line)(text)
