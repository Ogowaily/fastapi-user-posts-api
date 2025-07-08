from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.models import Post, User
from app.utils import hash
from app.database import Base, engine, SessionLocal
from app.schema import PostSchema, UserCreat, UserOut
from app.routers import post, user, auth
from app.dependencies import get_db
#main responsible for creating the FastAPI application and including the routers
# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", description="Get welcome message")
async def get_welcome_message():
    return {"message": "Welcome to FastAPI and SQLAlchemy"}

@app.get("/sqlalchemy", description="Get SQLAlchemy message")
async def get_sqlalchemy_message(db: Session = Depends(get_db)):
    return {"session": "Welcome to SQLAlchemy"}

# Include routers for posts, users, and authentication
# These routers handle the respective endpoints for each functionality
app.include_router(post.router, prefix="/api/v1", tags=["posts"])
app.include_router(user.router, prefix="/api/v1", tags=["users"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
