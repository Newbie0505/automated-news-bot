import os
import requests

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def test_and_send():
    # 1. Check if NewsAPI is working
    print(f"Fetching news...")
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    
    articles = response.get('articles', [])
    print(f"Found {len(articles)} articles.")

    if not articles:
        message = "⚠️ System Test: No news found, but connection is working!"
    else:
        top_story = articles[0].get('title')
        message = f"🚀 **Bot Live!**\n\nTop News: {top_story}"

    # 2. Check if Telegram is working
    print(f"Sending to Chat ID: {CHAT_ID}...")
    api_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    r = requests.post(api_url, data=payload)
    print(f"Telegram Response: {r.text}")

if __name__ == "__main__":
    test_and_send()
