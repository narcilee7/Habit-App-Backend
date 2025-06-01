from pydantic import BaseModel
from typing import Optional

class HabitCreate(BaseModel):
  user_id: int
  name: str
  description: Optional[str] = None

class HabitOut(BaseModel):
  id: int
  name: str
  description: Optional[str] = None

  class Config:
    orm_mode = True