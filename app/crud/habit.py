from sqlalchemy.orm import Session
from app.models.habit import Habit
from typing import Optional
from sqlalchemy import func

def create_habit(db: Session, user_id: int, title: str, color: str, description: Optional[str] = None, icon: str = "default_icon"):
    habit = Habit(
        user_id=user_id,
        title=title,
        description=description,
        color=color,
        icon=icon
    )
    db.add(habit)
    db.commit()
    db.refresh(habit)
    return habit

def get_user_habits(db: Session, user_id: int):
    return db.query(Habit).filter(Habit.user_id == user_id).all()

def update_habit(db: Session, habit_id: int, title: Optional[str] = None, description: Optional[str] = None, color: Optional[str] = None, icon: Optional[str] = None):
    habit = get_habit_by_id(db, habit_id)
    if not habit:
        return None

    if title is not None:
        setattr(habit, "title", title)
    if description is not None:
        # habit.description = description
        setattr(habit, "description", description)
    if color is not None:
        # habit.color = color
        setattr(habit, "color", color)
    if icon is not None:
        # habit.icon = icon
        setattr(habit, "icon", icon)
    setattr(habit, "updated_at", func.now())

    db.commit()
    db.refresh(habit)
    return habit

def delete_habit(db: Session, habit_id: int):
    habit = get_habit_by_id(db, habit_id)
    if not habit:
        return None

    db.delete(habit)
    db.commit()
    return habit

def get_habits_count(db: Session, user_id: int):
    return db.query(Habit).filter(Habit.user_id == user_id).count()

def get_habit_by_id(db: Session, habit_id: int):
    return db.query(Habit).filter(Habit.id == habit_id).first()