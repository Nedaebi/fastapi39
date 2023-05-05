import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/config.py")
from config import settings



# SQLALECHEMY_DATABASE_URL="postgresql://postgres:1366158@localhost:5432/fastapi"
SQLALECHEMY_DATABASE_URL =f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine=create_engine(SQLALECHEMY_DATABASE_URL)    #CONNECTION
Sessionlocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base= declarative_base()

def get_db():
    db=Sessionlocal()
    try:
        yield db 
    finally:
        db.close()

# just use this when we use sql 
# while True:
#     try:
#         conn=psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="1366158", cursor_factory=RealDictCursor)
#         cursor= conn.cursor()
#         print('database connected')
#         break
#     except Exception as error:
#         print("connection failed")
#         print("Error:", error)
#         time.sleep(2)