from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.user import User as UserModel
from app.core.security import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user_id(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
    ) -> int:
    payload = verify_token(token)
    email = payload.get("sub")

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user_id = db.query(UserModel.id).filter(UserModel.email == email).scalar()
    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user_id
