from sqlalchemy.orm import Session
from app.models.habit import Habit
from typing import Optional

def create_habit(db: Session, user_id: int, name: str, description: Optional[str] = None):
    habit = Habit(user_id=user_id, name=name, description=description)
    db.add(habit)
    db.commit()
    db.refresh(habit)
    return habit

def get_user_habits(db: Session, user_id: int):
    return db.query(Habit).filter(Habit.user_id == user_id).all()
