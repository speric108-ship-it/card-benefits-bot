"""Sends collected articles to Claude API for a Chinese summary."""
import os
import requests


def summarize(items):
    if not items:
        return "🟢 本期檢查 — 沒有跟亞洲里程相關的新消息。"

    api_key = os.environ["ANTHROPIC_API_KEY"]

    articles = []
    for it in items:
        articles.append(
            "標題: " + it["title"] + "\n"
            "來源: " + it["source"] + "\n"
            "分類: " + ", ".join(it["buckets"]) + "\n"
            "相關卡片: " + ", ".join(it["cards"]) + "\n"
            "連結: " + it["link"] + "\n"
            "摘要: " + it["summary"][:800] + "\n"
        )

    article_text = "\n---\n".join(articles)

    prompt = (
        "你是專精亞洲航線里程的信用卡顧問。\n\n"
        "用戶關注的路線：美國飛台灣、日本、中國大陸（含轉機選項）\n"
        "用戶持有的卡：Chase Sapphire Preferred、BoA Atmos Rewards、Amex、Citi\n\n"
        "以下是本期收集到的相關文章：\n\n"
        + article_text + "\n\n"
        "請用繁體中文整理一份「亞洲里程快報」，重點放在：\n"
        "- 哪些轉點優惠對飛亞洲最有用（例如轉 ANA、長榮、國泰、日航、大韓等）\n"
        "- 亞洲線的里程票好消息（兌換標準變動、新航線、甜蜜點）\n"
        "- 住宿點數跟亞洲旅行相關的優惠（日本飯店、台灣飯店等）\n"
        "- 快到期的優惠要提醒\n\n"
        "格式規則：\n"
        "- 每張卡 / 每個消息用 1-3 句話講完，不要囉唆\n"
        "- 用 emoji 標記重要程度：🔥 必搶、⏰ 快到期、✈️ 里程相關、🏨 住宿相關\n"
        "- 最後附上原文連結\n"
        "- 總長度不超過 1500 字\n"
        "- 如果某篇文章跟亞洲里程無關就直接跳過不提\n"
        "- 語氣簡潔像朋友傳訊息"
    )

    r = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": "claude-sonnet-4-6",
            "max_tokens": 1500,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60,
    )
    r.raise_for_status()
    return r.json()["content"][0]["text"]
