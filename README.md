AI News Intelligence Bot
A lightweight, always-on Telegram bot that serves as a personal research assistant — delivering real-time, topic-specific news headlines on demand.

Live Demo
Try it instantly on Telegram: @YourBotUsername

Features
FeatureDescriptionOn-Demand SearchRun /news <topic> to instantly retrieve the 3 most recent articles on any subjectReal-Time HeadlinesPowered by NewsAPI to surface the latest global coverage24/7 UptimeDeployed on Render with a Flask keep-alive server to prevent idle shutdown

Tech Stack
LayerTechnologyLanguagePython 3.xBot FrameworkpyTelegramBotAPI (Telegram Bot API)News DataNewsAPIWeb ServerFlaskHostingRender

Getting Started
Prerequisites

Python 3.8+
A Telegram Bot Token
A NewsAPI Key

Installation
bashgit clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
Configuration
Create a .env file in the root directory:
envTELEGRAM_BOT_TOKEN=your_telegram_token_here
NEWS_API_KEY=your_newsapi_key_here
Running Locally
bashpython bot.py

Usage
CommandDescription/startInitialize the bot and view available commands/news <topic>Fetch the latest 3 headlines on a given topic
Example:
/news artificial intelligence

Deployment
This project is configured for one-click deployment on Render. The embedded Flask server pings the service at regular intervals to maintain uptime on the free tier.

License
Distributed under the MIT License. See LICENSE for details.
## 📸 Screenshots
![Bot Demo]
(<img width="746" height="1600" alt="image" src="https://github.com/user-attachments/assets/7cbb9b7c-6c7c-4633-82ba-e4d2fedc300e" />) 
*(<img width="820" height="1600" alt="image" src="https://github.com/user-attachments/assets/ecee9fac-0e83-47ba-8003-8936f9fa240b" />
)*
