from pydantic import BaseModel
from typing import Optional

class HabitCreate(BaseModel):
  user_id: int
  title: str
  description: Optional[str] = None
  color: str
  icon: str

  class Config:
    orm_mode = True
    from_attributes = True

class HabitOut(BaseModel):
  id: int
  name: str
  description: Optional[str] = None
  color: str
  icon: str
  created_at: str

  class Config:
    orm_mode = True
    

class HabitUpdate(BaseModel):
  title: Optional[str] = None
  description: Optional[str] = None
  color: Optional[str] = None
  icon: Optional[str] = None

  class Config:
    orm_mode = True
    from_attributes = True

class HabitDelete(BaseModel):
  id: int

  class Config:
    orm_mode = True
    from_attributes = True