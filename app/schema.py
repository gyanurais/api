from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

    class Config:
        orm_mode=True

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class Postcreate(Post):
    pass

class Postmeth(Post):
    id:int
    created_at: datetime
    owner_id:int
    owner:UserOut

    class Config:
        orm_mode=True
    
class PostOut(BaseModel):
    Post:Postmeth
    votes:int

    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email: EmailStr
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id: Optional[str]=None
    
class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)