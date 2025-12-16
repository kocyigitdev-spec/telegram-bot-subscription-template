from telegram import Update
from telegram.ext import ContextTypes
from src.database import Database

db = Database()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command"""
    user = update.effective_user
    
    # Save user
    db.add_user(user.id, user.username, user.first_name)
    
    welcome_text = f"""
👋 Hello {user.first_name}!

I'm a subscription notification bot.

Available commands:
/subscribe - Subscribe to notifications
/unsubscribe - Unsubscribe
/status - Check subscription status
/help - Help

Use /subscribe to get started!
"""
    await update.message.reply_text(welcome_text)


async def subscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Subscribe command"""
    user_id = update.effective_user.id
    db.subscribe_user(user_id)
    
    await update.message.reply_text(
        "✅ Successfully subscribed! You will now receive notifications."
    )


async def unsubscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Unsubscribe command"""
    user_id = update.effective_user.id
    db.unsubscribe_user(user_id)
    
    await update.message.reply_text(
        "❌ Unsubscribed. You will no longer receive notifications.\n"
        "Use /subscribe to subscribe again."
    )


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Status check"""
    user_id = update.effective_user.id
    user = db.get_user(user_id)
    
    if user and user.is_subscribed:
        status_text = "✅ Subscription: Active"
    else:
        status_text = "❌ Subscription: Inactive"
    
    await update.message.reply_text(status_text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    help_text = """
📖 Available Commands:

👤 User Commands:
/start - Start the bot
/subscribe - Subscribe to notifications
/unsubscribe - Unsubscribe
/status - Check subscription status
/help - This help message

❓ Questions: @your_username
"""
    await update.message.reply_text(help_text)