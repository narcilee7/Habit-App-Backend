from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import get_password_hash, verify_password

def create_user(db: Session, username: str, email: str, password: str):
  hashed_pwd = get_password_hash(password)
  user = User(
    username=username,
    email=email,
    hashed_password=hashed_pwd,
  )
  db.add(user)
  db.commit()
  db.refresh(user)
  return user

def get_user_by_username(db: Session, username: str):
  return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
  return db.query(User).filter(User.email == email).first()

def authenticate_user(db: Session, username: str, password: str):
  user = get_user_by_username(db, username)
  if user and verify_password(password, user.hashed_password):
    return user
  return None
