
from fastapi import APIRouter, Depends, HTTPException, status
from blog import  database, models, auth_token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog.hashing import Hash


router = APIRouter()

@router.post("/login", tags=["authentication"])
def login(request: OAuth2PasswordRequestForm= Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.user_name == request.username).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")
    access_token = auth_token.create_access_token(data={"sub": user.user_name})
    return {'access_token': access_token, "token_type": "bearer"}