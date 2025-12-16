import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from src.config import Config
from src.database import Database
from src.handlers.user_handlers import (
    start_command,
    subscribe_command,
    unsubscribe_command,
    status_command,
    help_command,
)
from src.handlers.admin_handlers import (
    broadcast_command,
    stats_command,
    users_command,
)

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    """Start the bot"""
    # Validate config
    Config.validate()
    
    # Initialize database
    db = Database()
    db.create_tables()
    
    # Build application
    application = Application.builder().token(Config.BOT_TOKEN).build()
    
    # User handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("subscribe", subscribe_command))
    application.add_handler(CommandHandler("unsubscribe", unsubscribe_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("help", help_command))
    
    # Admin handlers
    application.add_handler(CommandHandler("broadcast", broadcast_command))
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("users", users_command))
    
    # Start bot
    logger.info("Bot starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()