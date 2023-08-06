from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from dotenv import find_dotenv , load_dotenv
# import os
from config import setting
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time


# this can be done by using dotenv module
# load_dotenv(find_dotenv())
# username = os.environ.get('dusername')
# password = os.environ.get('dpassword')
# hostname = os.environ.get('dhostname')
# database_name = os.environ.get('dname')

# this is done by config file
username = setting.dusername
password = setting.dpassword
hostname = setting.dhostname
database_name = setting.dname

SQL_DATABASE_URL = f'postgresql://{username}:{password}@{hostname}/{database_name}'

engine = create_engine(SQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

#dependency for talking to the database not connecting
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# #loop for connecting to the database
# there is no need for this code in sqlalchemy
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', database= 'fastapi', user= 'postgres', password = 'spiderman',
#                                       cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection succesfull")
#         break
#     except Exception as error:
#         print("database connection was unsuccesfull")
#         print("trying to connect again...")
#         time.sleep(2)