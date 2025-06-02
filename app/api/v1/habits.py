from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.core.db import get_db
from app.deps.auth import get_current_user_id
from app.models.user import User as UserModel

router = APIRouter(prefix="/habits", tags=["habits"])


@router.post("/create", response_model=schemas.habit.HabitOut)
def create_habit(habit_in: schemas.habit.HabitCreate, db: Session = Depends(get_db)):
    current_user_id = habit_in.user_id
    if not current_user_id:
        raise HTTPException(status_code=400, detail="User ID is required")
    user = crud.user.get_user_by_id(db, user_id=current_user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.habit.create_habit(
        db,
        user_id=current_user_id,
        title=habit_in.title,
        color=habit_in.color,
        description=habit_in.description,
        icon=habit_in.icon,
    )


@router.get("/list", response_model=list[schemas.habit.HabitOut])
def get_habits(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id),
): 
    return crud.habit.get_user_habits(db, user_id=current_user_id)

@router.put("/update/{habit_id}", response_model=schemas.habit.HabitUpdate)
def update_habit(
    habit_id: int,
    habit_update: schemas.habit.HabitUpdate,
    db: Session = Depends(get_db),
):
    habit = crud.habit.get_habit_by_id(db, habit_id=habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")

    return crud.habit.update_habit(
        db,
        habit_id=habit_id,
        title=habit_update.title,
        description=habit_update.description,
        color=habit_update.color,
        icon=habit_update.icon,
    )

@router.delete("/delete/{habit_id}", response_model=schemas.habit.HabitDelete)
def delete_habit(
    habit_id: int,
    db: Session = Depends(get_db),
):
    habit = crud.habit.get_habit_by_id(db, habit_id=habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")

    deleted_habit = crud.habit.delete_habit(db, habit_id=habit_id)
    return delete_habit if deleted_habit else HTTPException(status_code=404, detail="Habit not found")

@router.get("/{habit_id}", response_model=schemas.habit.HabitOut)
def get_habit_by_id(
    habit_id: int,
    db: Session = Depends(get_db),
):
    habit = crud.habit.get_habit_by_id(db, habit_id=habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit

@router.get("/stat/count", response_model=int)
def get_habits_count(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id),
):
    return crud.habit.get_habits_count(db, user_id=current_user_id)