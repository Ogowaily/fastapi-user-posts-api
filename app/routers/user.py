import fastapi
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from app.models import Post, User
from fastapi.middleware.cors import CORSMiddleware
from app.utils import hash
from app.database import Base, engine, SessionLocal
from pydantic import BaseModel
from datetime import datetime
from app.schema import PostSchema, UserCreat, UserOut
from app.dependencies import get_db
#user router responsible for handling user-related operations




router = APIRouter()
#this router creates a new user
@router.post("/users", response_model=UserOut, description="Create a new user")
async def create_user(user: UserCreat, db: Session = Depends(get_db)):
    hashed_password =hash(user.password)
    user.password = hashed_password
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user     
    
     
    
 
#this endpoint retrieves users from the database by id
@router.get("/users{id}", response_model=UserOut, description="Get user by ID")
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user