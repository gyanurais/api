from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings


SQLALCHEMY_DATABASE_URL=f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', user='postgres', database='fastapi',
#                                 password='postgresql', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection was successfull")
#         break
#     except Exception as error:
#         print("database connection was failed")
#         print("error: ", error)
#         time.sleep(2)