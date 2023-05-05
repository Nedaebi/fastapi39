from fastapi import  Depends, status, HTTPException, APIRouter
from fastapi.security import  OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import schemas, models, utils, oauth2
router= APIRouter(tags=["Authentication"])

#using  OAuth2PasswordRequestForm Email is username
@router.post("/login", response_model=schemas.Token)
# async def login(user_credentials:schemas.user_response,db:Session=Depends(get_db)):
async def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
      # user= db.query(models.users).filter(models.users.Email==user_credentials.Email).first()
      user= db.query(models.users).filter(models.users.Email==user_credentials.username).first()
      if not user :
         raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "invalid credential")
      if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "invalid credential")
      access_token=oauth2.create_access_token(data={"user_id":user.id})
      print(user.id)
      return {"access_token": access_token, "token_type": "bearer"}
