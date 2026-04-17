import os
import requests
import telebot

# Load keys from environment variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

bot = telebot.TeleBot(TOKEN)

# Welcome message
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🤖 **Welcome to the Interactive News Bot!**\n\n"
        "I can find news on any topic for you.\n"
        "Just type: `/news <topic>`\n"
        "Example: `/news cryptocurrency` or `/news cricket`"
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

# The "Researcher" logic
@bot.message_handler(commands=['news'])
def get_custom_news(message):
    # Get the topic from the user (everything after /news)
    query = message.text.replace('/news ', '').strip()
    
    if not query or query == "/news":
        bot.reply_to(message, "Please provide a topic! Example: `/news space`")
        return

    bot.send_message(message.chat.id, f"🔎 Searching for the latest on **{query}**...", parse_mode='Markdown')
    
    # Query NewsAPI specifically for what the user typed
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&pageSize=3&language=en&apiKey={NEWS_API_KEY}"
    
    try:
        response = requests.get(url).json()
        articles = response.get('articles', [])

        if not articles:
            bot.reply_to(message, f"❌ I couldn't find any recent news about '{query}'.")
            return

        for art in articles:
            news_message = (
                f"🌟 **{art['title']}**\n"
                f"📝 {art['description'][:150]}...\n"
                f"🔗 [Read More]({art['url']})"
            )
            bot.send_message(message.chat.id, news_message, parse_mode='Markdown', disable_web_page_preview=False)
            
    except Exception as e:
        bot.reply_to(message, "⚠️ Something went wrong while fetching the news.")

# This keeps the bot listening 24/7
print("Bot is starting...")
bot.infinity_polling()
