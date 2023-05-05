import sys
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException,status
from jose import JWTError, jwt
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/schemas.py")
import schemas
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/models.py")
import models
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/database.py")
from database import get_db
from datetime import datetime, timedelta
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/config.py")
from config import settings

oath2_scheme= OAuth2PasswordBearer(tokenUrl="login")
# SECRET_KEY= "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM= "HS256"
ACCSESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
# ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCSESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return  encoded_jwt

def verify_access_token(token:str, credential_exception):
     try:
         payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
         id:str= payload.get("user_id")
         if not id :
              raise credential_exception
         token_data= schemas.Tokendata(id=id)
     except JWTError:
          raise credential_exception
     return token_data

def get_current_user (token:str=Depends(oath2_scheme), db:Session=Depends(get_db)):
     credential_exception= HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "could not validate credentials",
     headers={"www-Authenticate":"Bearer"})
     token = verify_access_token(token,credential_exception)
     print(token)
     user=db.query(models.users).filter(models.users.id==token.id).first()
     print(user.Email)
     return user