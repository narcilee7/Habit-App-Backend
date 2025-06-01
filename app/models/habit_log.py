from sqlalchemy import Column, String, DateTime, func, BigInteger, ForeignKey
from app.core.db import Base

class HabitLog(Base):
   __tablename__ = 'habit_logs'
   
   id = Column(BigInteger, primary_key=True, index=True)
   habit_id = Column(BigInteger, ForeignKey('habits.id'), index=True, nullable=False)
   log_date = Column(DateTime, nullable=False)
   status = Column(String(20))  # completed / skipped / failed
   created_at = Column(DateTime, server_default=func.now(), nullable=False)