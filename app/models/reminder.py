from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, BigInteger, func, Text
from app.core.db import Base

class Reminder(Base):
    __tablename__ = 'reminders'

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), index=True, nullable=False)
    habit_id = Column(BigInteger, ForeignKey('habits.id'), index=True, nullable=False)
    message = Column(Text, nullable=False)  # 提醒内容
    remind_at = Column(DateTime, nullable=False)  # 提醒时间
    is_recurring = Column(Boolean, default=False)  # 是否重复提醒
    recurring_pattern = Column(String(50))  # 重复规则，如 daily, weekly, cron 表达式
    is_sent = Column(Boolean, default=False)  # 是否已发送
    is_clicked = Column(Boolean, default=False)  # 用户是否点击了提醒
    sent_at = Column(DateTime)  # 发送时间
    clicked_at = Column(DateTime)  # 点击时间
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)