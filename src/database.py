from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from src.config import Config

Base = declarative_base()


class User(Base):
    """User model"""
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    is_subscribed = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Database:
    """Database operations"""
    
    def __init__(self):
        self.engine = create_engine(Config.DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)
    
    def create_tables(self):
        """Create tables"""
        Base.metadata.create_all(self.engine)
    
    def add_user(self, user_id: int, username: str = None, first_name: str = None):
        """Add or update user"""
        session = self.Session()
        user = session.query(User).filter_by(user_id=user_id).first()
        
        if user:
            user.username = username
            user.first_name = first_name
            user.updated_at = datetime.utcnow()
        else:
            user = User(
                user_id=user_id,
                username=username,
                first_name=first_name,
                is_subscribed=True
            )
            session.add(user)
        
        session.commit()
        session.close()
    
    def subscribe_user(self, user_id: int):
        """Subscribe user"""
        session = self.Session()
        user = session.query(User).filter_by(user_id=user_id).first()
        if user:
            user.is_subscribed = True
            session.commit()
        session.close()
    
    def unsubscribe_user(self, user_id: int):
        """Unsubscribe user"""
        session = self.Session()
        user = session.query(User).filter_by(user_id=user_id).first()
        if user:
            user.is_subscribed = False
            session.commit()
        session.close()
    
    def get_user(self, user_id: int):
        """Get user info"""
        session = self.Session()
        user = session.query(User).filter_by(user_id=user_id).first()
        session.close()
        return user
    
    def get_subscribed_users(self):
        """Get subscribed users"""
        session = self.Session()
        users = session.query(User).filter_by(is_subscribed=True).all()
        session.close()
        return users
    
    def get_stats(self):
        """Get statistics"""
        session = self.Session()
        total = session.query(User).count()
        subscribed = session.query(User).filter_by(is_subscribed=True).count()
        session.close()
        return {'total': total, 'subscribed': subscribed}