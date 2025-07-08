from app.database import SessionLocal
#responsible for providing the database session to the FastAPI application
# Dependency to get the database session
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()