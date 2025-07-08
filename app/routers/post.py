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
from app.auth2 import get_current_user

# post router responsible for handling post-related operations
router = APIRouter()

@router.get("/posts", response_model=list[PostSchema], description="Get all posts")
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts

@router.post("/posts", response_model=PostSchema, description="Create a new post")
async def create_post(
    post: PostSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    new_post = Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post