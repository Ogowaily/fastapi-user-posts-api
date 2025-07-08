from app.database import Base, engine
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean,func,ForeignKey  # Corrected 'boolean' to 'Boolean'
#respon for creating the table 
class Post(Base):
    __tablename__ = "post_table2"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Added autoincrement=True
    title = Column(String, index=True)
    description = Column(String, index=True)
    published = Column(DateTime, index=True)
    rating = Column(Float, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True)  # Corrected 'boolean' to 'Boolean'
    created_at = Column(DateTime, index=True)  # New column for created timestamp
    user_id = Column(Integer, index=True)  # Foreign key to User table
    user_id = Column(Integer, ForeignKey("user_table.id"))  # Uncomment if you want to establish a relationship with User table    
    
class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Added autoincrement=True
    # name = Column(String, index=True,nullable=False)
    email = Column(String, unique=True, index=True,nullable=False)
    password = Column(String,nullable=False)
    created_at = Column(DateTime, index=True,default=func.now())  # New column for created timestamp    