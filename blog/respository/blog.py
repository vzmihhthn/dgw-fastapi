from .. import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def get_all_blogs(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(request : schemas.Blog, db:Session):
    new_blog = models.Blog(blog_title=request.title, blog_body=request.body, user_id=2 )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blog_id(id, db: Session):
    blog_id = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog {id} not found")
    return blog_id

def delete_blog(id, db: Session):
    blog_id = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog_id.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog {id} not found")
    blog_id.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Blog {id} deleted"}

def update_blog(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog {id} not found")
    blog.update(request.dict())
    db.commit()
    return {"message": f"Blog {id} updated successfully"}