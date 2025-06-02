from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.core.db import get_db
from app.deps.auth import get_current_user_id


router = APIRouter(prefix="/records", tags=["records"])

@router.post("/create", response_model=schemas.record.RecordOut)
def create_record(
    record_in: schemas.record.RecordCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id),
):
    habit = crud.habit.get_habit_by_id(db, habit_id=record_in.habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    return crud.record.create_record(
        db,
        user_id=current_user_id,
        habit_id=record_in.habit_id,
        record_date=record_in.record_date,
    )


@router.get("/list", response_model=list[schemas.record.RecordOut])
def get_records(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id),
):
    return crud.record.get_user_records(db, user_id=current_user_id)