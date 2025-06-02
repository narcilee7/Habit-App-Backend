from datetime import datetime
from pydantic import BaseModel, Field

class RecordCreate(BaseModel):
  habit_id: int
  user_id: int
  record_date: datetime = Field(default_factory=datetime.now)

class RecordOut(BaseModel):
  id: int
  habit_id: int
  user_id: int
  record_date: datetime = Field(default_factory=datetime.now)
  created_at: datetime = Field(default_factory=datetime.now)

  class Config:
    orm_mode = True
    from_attributes = True