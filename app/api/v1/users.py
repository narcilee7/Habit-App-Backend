from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.core.db import get_db
from app.core import security


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=schemas.user.UserOut)
def register(user_in: schemas.user.UserCreate, db: Session = Depends(get_db)):
  db_user = crud.user.get_user_by_username(db, user_in.username)
  if db_user:
    raise HTTPException(status_code=400, detail="Username already registered")
  db_email = crud.user.get_user_by_email(db, user_in.email)
  if db_email:
    raise HTTPException(status_code=400, detail="Email already registered")
  return crud.user.create_user(
    db,
    user_in.username,
    user_in.email,
    user_in.password
  )

@router.post("/login")
def login(user_in: schemas.user.UserLogin, db: Session = Depends(get_db)):
  user = crud.user.authenticate_user(db, user_in.email, user_in.password)
  if not user:
    raise HTTPException(status_code=401, detail="Invalid credentials")
  
  access_token = security.create_access_token(data={"sub": user.email})
  return {"access_token": access_token, "token_type": "bearer", "user": user}