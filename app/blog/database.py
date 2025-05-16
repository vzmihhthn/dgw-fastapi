from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL

def get_db_url():
    return URL.create(
        drivername="postgresql+psycopg2",
        username="postgres",
        password="itintern",
        host="localhost",
        port=5432,
        database="FastAPI_DB"
    )

DB_URL = get_db_url()

engine = create_engine(DB_URL)

SessionLocal = sessionmaker( bind=engine)

Base = declarative_base

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()