from sqlalchemy.orm import Session
from app.models.records import Record
from datetime import datetime

def create_record(db: Session, user_id: int, habit_id: int, record_date: datetime):
    record = Record(
        user_id=user_id,
        habit_id=habit_id,
        record_date=record_date
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_user_records(db: Session, user_id: int):
    return db.query(Record).filter(Record.user_id == user_id).all()

def get_record_by_id(db: Session, record_id: int):
    return db.query(Record).filter(Record.id == record_id).first()