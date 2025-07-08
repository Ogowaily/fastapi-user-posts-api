from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database import SessionLocal, Base, engine
from app.dependencies import get_db
from app.schema import Token
from app.models import User
from app.utils import verify_password
from app.auth2 import create_access_token

# auth router responsible for handling user authentication
router = APIRouter()
# This router handles user login
# This endpoint allows users to log in by providing their email and password
@router.post("/login", description="User login", response_model=Token)
async def login(
    user: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.email == user.username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}



