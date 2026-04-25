"""Sends collected articles to Claude API for a Chinese summary."""
import os, requests, json

def summarize(items):
    if not items:
        return "🟢 本週信用卡檢查 — 這週沒有跟你的卡相關的新消息。"

    api_key = os.environ["ANTHROPIC_API_KEY"]

    articles = []
    for it in items:
        articles.append(
            f"標題: {it['title']}\n"
            f"來源: {it['source']}\n"
            f"分類: {', '.join(it['buckets'])}\n"
            f"相關卡片: {', '.join(it['cards'])}\n"
            f"連結: {it['link']}\n"
            f"摘要: {it['summary'][:800]}\n"
        )

    article_text = "\n---\n".join(articles)

    prompt = f"""你是一個專業的信用卡顧問。我持有以下信用卡：
1. Chase Sapphire Preferred（年費 $95）
2. Bank of America Atmos Rewards（前身是 Alaska Airlines Visa）

以下是本週從各大信用卡部落格和 Reddit 收集到的、跟我的卡相關的文章：

{article_text}

請用繁體中文幫我整理一份「本週信用卡行動指南」，格式如下：

📬 本週信用卡行動指南

⏰ 【趕快行動】即將到期的優惠
（列出快到期的優惠，告訴我具體該怎麼做才能把握）

🆕 【新消息】本週新福利 / 新優惠
（用白話文解釋每個新福利對我有什麼好處，值不值得用）

⚠️ 【注意】福利縮水 / 變動
（如果有卡片福利變差的消息，分析我是否該考慮關卡，以及關卡前要注意什麼才最划算）

💡 【建議】本週行動清單
（根據以上所有資訊，給我一個簡單的 to-do list，告訴我這週該做什麼）

規則：
- 全部用繁體中文
- 不要只給我連結，要用你自己的話解釋重點
- 語氣像朋友在聊天一樣，不要太正式
- 如果某個分類沒有相關消息就跳過，不要硬寫
- 最後可以附上原文連結讓我參考，但重點是你的分析和建議
- 總長度控制在 LINE 訊息容易閱讀的範圍（不超過 2000 字）"""

    r = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 2000,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60,
    )
    r.raise_for_status()
    data = r.json()
    return data["content"][0]["text"]
