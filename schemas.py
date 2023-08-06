from pydantic import BaseModel , EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    
    title : str
    content : str
    published : bool = True
    
class PostCreate(PostBase):
    pass
    
    
class POST(PostBase):
    id : int
    title : str
    content : str
    published : bool 
    owner_id : str
    # owner : UserOut   wont work till i get the userout class before post class(current class)    

    class config:
        orm_mode = True
        
class UserBase(BaseModel):
    
    email : EmailStr
    password : str
    
class UserCreate(UserBase):
    pass

class UserOut(BaseModel):
    
    id : int
    email : EmailStr
    
    class config:
        orm_mode = True
        
class login_cred(BaseModel):
    email: EmailStr
    password : str
    
class Token(BaseModel):
    access_token: str
    token_type : str
    
class Tokendata(BaseModel):
    id : Optional[str] = None

class Vote(BaseModel):
    post_id : int
    dir : conint(le=1)