import os
import requests

# Fetching the secrets we saved in GitHub Settings
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def get_tech_news():
    # Fetching top technology headlines from NewsAPI
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get('articles', [])[:5] # Take the top 5
    
    report = "🚀 **Daily Tech Intelligence** 🚀\n\n"
    if not articles:
        return "No news found today."
        
    for art in articles:
        title = art.get('title')
        url = art.get('url')
        report += f"🔹 {title}\n🔗 {url}\n\n"
    return report

def send_telegram_msg(message):
    # Sending the report to your Telegram bot
    api_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    requests.post(api_url, data=payload)

if __name__ == "__main__":
    news_report = get_tech_news()
    send_telegram_msg(news_report)
