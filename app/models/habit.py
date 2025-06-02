from sqlalchemy import Column, Integer, BigInteger, String, Text, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from app.core.db import Base

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    color = Column(String(20), nullable=False)
    icon = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship("User", back_populates="habits")
