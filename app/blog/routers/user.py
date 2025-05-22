# gọi hàm tạo bảng -> schema 
from typing import List
from fastapi import Depends, FastAPI, status, Response, APIRouter
from .. import schemas, database,oauth2
from sqlalchemy.orm import Session
from ..respository import user
from middleware.logger import logger


app = FastAPI()

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("/{id}", status_code=status.HTTP_200_OK,response_model=schemas.ShowUser ) #get user by id
def get_user_id(id, response: Response, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    logger.info(f"Fetching user with ID: {id}")
    return user.get_user_id(id, db)

@router.post("/", response_model= schemas.User, status_code=status.HTTP_201_CREATED ) #add user
def create_user(request: schemas.User, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):   
    logger.info("Creating a new user")
    return user.create_user(request, db)

@router.get("/", response_model=list[schemas.ShowUser], status_code=status.HTTP_200_OK ) #get all users
def get_all_users(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    logger.info("Fetching all users")
    return user.get_all_users(db)

@app.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT )
def delete_user(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    logger.info(f"Deleting user with ID: {id}")
    return user.delete_user(id, db)

@app.put('/user/{id}', status_code=status.HTTP_202_ACCEPTED )
def update_user(id, request: schemas.User,db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    logger.info(f"Updating user with ID: {id}")
    return user.update_user(id, request, db)