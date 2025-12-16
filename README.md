# Telegram Subscription Bot

A simple and clean Telegram bot for managing user subscriptions and sending broadcast messages. Built this to learn the python-telegram-bot library and sharing it as a template for anyone who needs similar functionality.

## What it does

This bot helps you manage a subscriber list and send messages to all subscribers at once. Think of it like a newsletter system but on Telegram.

**For users:**
- Subscribe to get notifications
- Unsubscribe anytime
- Check their subscription status

**For admins:**
- Send messages to all subscribers
- See how many people are subscribed
- View the subscriber list

## Tech stuff

- Python 3.11+
- python-telegram-bot for the Telegram API
- SQLAlchemy for database stuff
- SQLite (or PostgreSQL if you prefer)

## Getting started

You'll need a bot token from [@BotFather](https://t.me/BotFather) on Telegram and your Telegram user ID from [@userinfobot](https://t.me/userinfobot).

**Setup:**
```bash
# Clone it
git clone https://github.com/yourusername/telegram-bot-subscription-template.git
cd telegram-bot-subscription-template

# Make a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Mac/Linux

# Install stuff
pip install -r requirements.txt

# Copy .env.example to .env and add your bot token and admin ID
# Then run it
python -m src.bot

## Commands

**Everyone can use:**
- `/start` - Get started
- `/subscribe` - Start receiving messages
- `/unsubscribe` - Stop receiving messages
- `/status` - Check if you're subscribed
- `/help` - Show commands

**Admin only:**
- `/broadcast <message>` - Send to all subscribers
- `/stats` - See subscriber count
- `/users` - List subscribers

## Project structure

src/
├── bot.py              # Main bot code
├── config.py           # Settings
├── database.py         # Database stuff
├── handlers/           # Command handlers
│   ├── user_handlers.py
│   └── admin_handlers.py
└── utils/
    └── decorators.py   # Admin check decorator

## Config

Create a `.env` file:
```
BOT_TOKEN=your_bot_token_here
ADMIN_IDS=your_telegram_id
DATABASE_URL=sqlite:///bot.db
```

You can add multiple admin IDs separated by commas: `ADMIN_IDS=123456789,987654321`

## Running with Docker

If you want to use Docker:
bash
docker build -t telegram-bot .
docker run -d --env-file .env telegram-bot


## What I learned

Built this while learning async Python and the Telegram Bot API. The decorator pattern for admin commands was particularly interesting. SQLAlchemy made database handling pretty straightforward.

## Contributing

Found a bug or want to add something? Feel free to open an issue or PR. This is a learning project so I'm open to suggestions and improvements.

## License

MIT - use it however you want.

## Notes

This is a basic template. Depending on your use case, you might want to add:
- Rate limiting for broadcasts
- Message scheduling
- User preferences
- Rich media support
- Multiple admin roles
- Analytics

The code is commented and structured to be easy to modify.

If you use this for something cool, let me know! Always curious to see what people build.