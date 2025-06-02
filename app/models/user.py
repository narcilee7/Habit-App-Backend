from sqlalchemy import Column, BigInteger, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.core.db import Base

class User(Base):
  __tablename__ = 'users'

  id = Column(BigInteger, primary_key=True, index=True)
  username = Column(String(50), unique=True, index=True, nullable=False)
  email = Column(String(100), unique=True, index=True, nullable=False)
  hashed_password = Column(String(255), nullable=False)
  avatar_url = Column(String(255))
  created_at = Column(DateTime, server_default=func.now(), nullable=False)
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
  
  habits = relationship("Habit", back_populates="user")
  records = relationship("Record", back_populates="user", cascade="all, delete-orphan")