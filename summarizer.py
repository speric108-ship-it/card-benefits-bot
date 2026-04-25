"""Sends collected articles to Claude API for a Chinese summary."""
import os, requests

def summarize(items):
    if not items:
        return "🟢 本期檢查 — 沒有跟亞洲里程相關的新消息。"

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

    prompt = f"""你是專精亞洲航線里程的信用卡顧問。

用戶關注的路線：美國飛台灣、日本、中國大陸（含轉機選項）
用戶持有的卡：Chase Sapphire Preferred、BoA Atmos Rewards、Amex、Citi

以下是本期收集到的相關文章：

{article_text}

請用繁體中文整理一份「亞洲里程快報」，重點放在：
- 哪些轉點優惠對飛亞洲最有用（例如轉 ANA、長榮、國泰、日航、大韓等）
- 亞洲線的里程票好消息（兌換標準變動、新航線、甜蜜點）
- 住宿點數跟亞洲旅行相關的優惠（日本飯店、台灣飯店等）
- 快到期的優惠要提醒

格式規則：
- 每張卡 / 每個消息用 1-3 句話講完，不要囉唆
