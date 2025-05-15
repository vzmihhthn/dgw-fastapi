from typing import List, Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, DateTime, Enum, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .database import DB_URL, engine, Base
from sqlalchemy.orm import relationship
import uuid
import enum


engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Blog(Base):
    __tablename__ = "blogs"
    blog_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id")) # tạo khóa ngoại giữa bảng Blog và bảng User
    blog_title = Column(String, index=True)
    blog_body = Column(String, index=True)
    
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



# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     password = Column(String, index=True)

#     blogs = relationship("Blog", back_populates="author") # tạo mối quan hệ giữa bảng User và bảng Blog


