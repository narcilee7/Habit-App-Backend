from app.core.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, func

class Record(Base):
  __tablename__ = 'records'

  id = Column(BigInteger, primary_key=True, index=True)
  habit_id = Column(BigInteger, ForeignKey('habits.id'), nullable=False)
  user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
  record_date = Column(DateTime, server_default=func.now(), nullable=False)
  created_at = Column(DateTime, server_default=func.now(), nullable=False)

  user = relationship("User", back_populates="records")
  habit = relationship("Habit", back_populates="records")