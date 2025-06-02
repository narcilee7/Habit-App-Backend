from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
  username: str
  email: EmailStr
  password: str

class UserLogin(BaseModel):
  email: EmailStr
  password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    avatar_url: str | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True