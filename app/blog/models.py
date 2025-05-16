from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, func
from sqlalchemy.ext.declarative import declarative_base
from blog.database import Base ,engine
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()

class Blog(Base):
    __tablename__ = "blogs"
    blog_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id")) # tạo khóa ngoại giữa bảng Blog và bảng User
    title = Column(String, index=True)
    body = Column(String, index=True)
    
    author = relationship("User", back_populates="blogs") # tạo mối quan hệ giữa bảng Blog và bảng User

class genderEnum(enum.Enum):# tạo enum cho giới tính
    male = 'male'
    female = 'female'
    other = 'other'

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_code = Column(String, unique=True, index=True) # tạo mã người
    user_name = Column(String, unique=True, index=True) # tạo tên người dùng
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    date_of_birth = Column(String, index=True)
    gender = Column(Enum(genderEnum), index=True) # tạo enum cho giới tính
    password = Column(String, index=True) 
    created_at = Column(DateTime, server_default=func.now()) # tạo thời gian tạo người dùng
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now()) # tạo thời gian cập nhật người dùng
    is_active = Column(Integer, default=1) # tạo trạng thái người dùng

    blogs = relationship("Blog", back_populates="author") # tạo mối quan hệ giữa bảng User và bảng Blog

class BlogResponse(BaseModel):
    id: int
    title: str
    body: str

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    user_code: str
    name: str
    phone: str
    address: str
    is_active: bool
    blogs: List[BlogResponse] = []

    class Config:
        from_attributes = True

