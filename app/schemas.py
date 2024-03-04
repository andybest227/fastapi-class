
from datetime import datetime
from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, EmailStr, Field


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

class Post(PostBase):
    id:int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        orm_mode = True


# USERS SCHEMAS
class UserBase(BaseModel):
    email: EmailStr
    password: str
    

class CreateUser(BaseModel):
    email: EmailStr
    id: int
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(le=1)]
    