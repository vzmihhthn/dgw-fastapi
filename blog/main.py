from fastapi import  FastAPI
from blog.models import Base, engine
from .routers import blog, user


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)




