from fastapi import  FastAPI
from blog.models import Base, engine
from blog.routers import blog, user, authentication
from middleware.logger import log_request, logger

app = FastAPI()

app.middleware("http")(log_request)
logger.info("Starting the application...") 

@app.get("/")
def root():
    return {"message": "Welcome to the DGW FastAPI application!"}

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)

    





