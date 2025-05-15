# gọi hàm tạo bảng -> schema 
from typing import List
from fastapi import Depends, FastAPI, status, Response, APIRouter
from .. import schemas, database
from sqlalchemy.orm import Session
from ..respository import user

app = FastAPI()

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/", response_model= schemas.User, status_code=status.HTTP_201_CREATED ) #add user
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):   
    return user.create_user(request, db)

## 

# @router.post("/all", response_model=List[schemas.User], status_code=201)
# def create_all_users(request: List[schemas.User], db: Session = Depends(database.get_db)):
#     return user.create_all_users(request, db)


# @router.get("/", response_model=list[schemas.ShowUser], status_code=200 ) #get all users
# def get_users(request: schemas.User,db: Session = Depends(database.get_db)):
#     return user.get_users(request, db)


@router.get("/all", response_model=list[schemas.ShowUser], status_code=200 ) #get all users
def get_all_users(db: Session = Depends(database.get_db)):
    return user.get_all_users(db)


@router.get("/{id}", status_code=200,response_model=schemas.ShowUser ) #get user by id
def get_user_id(id, response: Response, db: Session = Depends(database.get_db)):
    return user.get_user_id(id, db)

@app.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT )
def delete_user(id, db: Session = Depends(database.get_db)):
    return user.delete_user(id, db)

@app.put('/user/{id}', status_code=status.HTTP_202_ACCEPTED )
def update_user(id, request: schemas.User,db: Session = Depends(database.get_db)):
    return user.update_user(id, request, db)