from sqlalchemy import Column, Integer, String, DateTime, func, BigInteger, Text, Boolean, ForeignKey
from app.core.db import Base

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), index=True, nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    frequency = Column(String(20))  # daily / weekly / monthly
    start_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
