from pydantic import BaseModel,EmailStr
from datetime import datetime
#responsible for defining the data models used in the application
#responsible for validating and serializing data
class PostSchema(BaseModel):
    title: str
    description: str
    published: datetime
    rating: float
    name: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
        
        
class PostCreateSchema(PostSchema):
    pass


        
class PostUpdateSchema(PostSchema):
    pass
        
        
        
class UserCreat(BaseModel):
    password: str
    email: EmailStr
    
    class Config:
        orm_mode = True
    
class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True    
    
            
            
class Userlogin(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        orm_mode = True            


class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        orm_mode = True
        
class TokenData(BaseModel):
    email: EmailStr
    class Config:
        orm_mode = True             