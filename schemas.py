from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from xmlrpc.client import Boolean
from pydantic import conint

class BPost(BaseModel):    #from pydantic lib
    title: str
    content: str
    # published: Boolean
    # rating: Optional[int]= None



class Userlogin (BaseModel):
    Email:EmailStr
    # password:str
    class Config:
        orm_mode = True

class Post(BPost):   
    owner_id:int
    created_at:datetime
    published: Boolean
    owner: Userlogin
    # id:int
    class Config:
        orm_mode = True

class postout(BaseModel):
    Post:Post
    votes_m:int
    class Config:
        orm_mode = True

#     class Config:
#         orm_mode = True

class createuser(BaseModel):
    Email:EmailStr
    password:str
    

class user_response(BaseModel):
    Email:EmailStr
    password:str
    class Config:
        orm_mode = True

class user_Login(BaseModel):
     username:EmailStr
     password:str



class Token(BaseModel):
    access_token:str
    token_type:str
    class Config:
        orm_mode = True

class Tokendata(BaseModel):
    id:Optional[str]=None
    # Email:EmailStr
    # password:str
    class Config:
        orm_mode = True

class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)

    