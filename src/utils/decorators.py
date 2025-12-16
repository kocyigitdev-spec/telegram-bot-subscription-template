from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
from src.config import Config


def admin_only(func):
    """Admin check decorator"""
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        
        if user_id not in Config.ADMIN_IDS:
            await update.message.reply_text(
                "⛔ You don't have permission to use this command!"
            )
            return
        
        return await func(update, context)
    
    return wrapper