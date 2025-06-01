from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.core.db import get_db
from app.deps.auth import get_current_user_id
from app.models.user import User as UserModel

router = APIRouter(prefix="/habits", tags=["habits"])



@router.post("/", response_model=schemas.habit.HabitOut)
def create_habit(habit_in: schemas.habit.HabitCreate, db: Session = Depends(get_db)):
    return crud.habit.create_habit(db, user_id=1, name=habit_in.name, description=habit_in.description)

@router.get("/", response_model=list[schemas.habit.HabitOut])
def get_habits(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id),
): 
    return crud.habit.get_user_habits(db, user_id=current_user_id)