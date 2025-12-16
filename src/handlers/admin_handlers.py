from telegram import Update
from telegram.ext import ContextTypes
from src.database import Database
from src.utils.decorators import admin_only

db = Database()


@admin_only
async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Broadcast message to all subscribers"""
    if not context.args:
        await update.message.reply_text(
            "❌ Usage: /broadcast <your message>"
        )
        return
    
    message = ' '.join(context.args)
    subscribers = db.get_subscribed_users()
    
    success = 0
    failed = 0
    
    for user in subscribers:
        try:
            await context.bot.send_message(
                chat_id=user.user_id,
                text=f"📢 Announcement:\n\n{message}"
            )
            success += 1
        except Exception as e:
            failed += 1
    
    await update.message.reply_text(
        f"✅ Broadcast completed!\n"
        f"Success: {success}\n"
        f"Failed: {failed}"
    )


@admin_only
async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show statistics"""
    stats = db.get_stats()
    
    stats_text = f"""
📊 Bot Statistics:

👥 Total Users: {stats['total']}
✅ Active Subscribers: {stats['subscribed']}
❌ Inactive Users: {stats['total'] - stats['subscribed']}
"""
    await update.message.reply_text(stats_text)


@admin_only
async def users_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """List users"""
    subscribers = db.get_subscribed_users()
    
    if not subscribers:
        await update.message.reply_text("No subscribers yet.")
        return
    
    user_list = "👥 Active Subscribers:\n\n"
    for user in subscribers[:20]:  # Show first 20
        username = f"@{user.username}" if user.username else "No username"
        user_list += f"• {user.first_name} ({username})\n"
    
    if len(subscribers) > 20:
        user_list += f"\n... and {len(subscribers) - 20} more"
    
    await update.message.reply_text(user_list)