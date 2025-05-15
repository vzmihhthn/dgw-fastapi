from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from datetime import datetime

class Blog(BaseModel):
    title: str
    body: str

    class Config:
        from_attribute = True # This is used to tell Pydantic to use the ORM mode

class GenderEnum(str, Enum): # This is used to create an enum for
    male = 'male'
    female= 'female'
    other = 'other'

class User(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    date_of_birth: Optional[str] = None
    gender : Optional[GenderEnum] = None # This is used to create an enum for
    user_name: str
    password: str

    class Config: # Config class is used to configure the Pydantic model
        from_attributes = True
    
    
class UserResponse(User):
    id: int
    user_code: Optional[str] 
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_active: Optional[bool] = True # This is used to create an enum for
    class Config: # Config class is used to configure the Pydantic model
        from_attributes = True

# class User(BaseModel):
#     name: str
#     email: str
#     password: str

#     class Config: # Config class is used to configure the Pydantic model
#         from_attribute = True

class ShowUser(BaseModel):
    user_code: str
    name: str
    email: str
    phone: str
    address: str
    date_of_birth: Optional[str] = None
    gender : Optional[GenderEnum] = None # This is used to create an enum for
    blogs: List[Blog] = [] # This is used to show the blogs of the user

      
class ShowBlog(BaseModel):
    title: str
    body: str
    author: ShowUser
    class Config:
        from_attributes = True # This is used to tell Pydantic to use the ORM mode