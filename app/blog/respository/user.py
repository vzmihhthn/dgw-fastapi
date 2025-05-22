# xử lý logic cho user
from typing import List
from .. import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..hashing import Hash

def get_all_users(db: Session):
    users = db.query(models.User).all()
    return users

def generate_user_code(db: Session) -> str:
    user_code = db.query(models.User).count() + 1
    return f"DGW{user_code:03d}"

def create_user(request: schemas.User, db: Session):
    new_user = models.User(
        user_code=generate_user_code(db),
        name=request.name,
        email=request.email,
        phone=request.phone,
        address=request.address,
        date_of_birth=request.date_of_birth,
        gender=request.gender.value,
        user_name=request.user_name,
        password=Hash.bcrypt(request.password),
        is_active=1
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# def create_user(request: schemas.User, db: Session):
#     new_user = models.User(name=request.name, email=request.email, password=request.password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


def create_all_users(request: List[schemas.User], db: Session):
    created_users = []
    for user in request:
        new_user = models.User(
            name=user.name,
            email=user.email,
            password=Hash.bcrypt(user.password)  
        )
        db.add(new_user)
        created_users.append(new_user)
    db.commit()
    for u in created_users:
        db.refresh(u)
    return created_users


def get_user_id(id, db: Session):
    user_id = db.query(models.User).filter(models.User.user_id == id).first()
    if not user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User {id} not found")
    return user_id


def delete_user(id, db: Session):
    user_id = db.query(models.User).filter(models.User.user_id == id)
    if not user_id.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User {id} not found")
    user_id.delete(synchronize_session=False)
    db.commit()
    return {"message": f"User {id} deleted"}

def update_user(id, request: schemas.User, db: Session):
    user = db.query(models.User).filter(models.User.user_id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User {id} not found")
    user.update(request.dict())
    db.commit()
    return {"message": f"User {id} updated successfully"}

