import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Bot configuration"""
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot.db')
    ADMIN_IDS = [int(id) for id in os.getenv('ADMIN_IDS', '').split(',') if id]
    
    @staticmethod
    def validate():
        """Validate required settings"""
        if not Config.BOT_TOKEN:
            raise ValueError("BOT_TOKEN not found!")
        if not Config.ADMIN_IDS:
            raise ValueError("At least one ADMIN_ID required!")