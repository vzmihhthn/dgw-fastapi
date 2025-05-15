from fastapi import Depends, FastAPI, status, Response,APIRouter
from .. import schemas, database
from sqlalchemy.orm import Session
from ..respository import blog

app = FastAPI()

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.post("/", status_code=status.HTTP_201_CREATED ) #add blog
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create_blog(request,db)

@router.get("/", response_model=list[schemas.ShowBlog], status_code=200 ) #get all blogs
def get_blogs(db: Session = Depends(database.get_db)): #get all blogs
    return blog.get_all_blogs(db)

@router.get("/{id}", status_code=200,response_model=schemas.Blog ) #get blog by id
def get_blog_id(id, response: Response, db: Session = Depends(database.get_db)): #get blog by id
    return blog.get_blog_id(id, db)

@app.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT )
def delete_blog(id, db: Session = Depends(database.get_db)):
    return blog.delete_blog(id, db)

@app.put('/{id}', status_code=status.HTTP_202_ACCEPTED )
def update_blog(id, request: schemas.Blog,db: Session = Depends(database.get_db)):
    return blog.update_blog(id, request, db)

