from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from xmlrpc.client import Boolean
import sys
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/models.py")
import models
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/post.py")
import post
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/user.py")
import user
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/auth.py")
import auth
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/vote.py")
import vote
from database import engine


# models.Base.metadata.create_all(bind=engine)
app = FastAPI()
post_1= [{"title":"sara", "content":"ebrahimpoor", "rating":4}]

origins=["https://www.google.com/"]
# origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


     

#     for post in post_1:
#         if post["rating"]==id:
#            post_update=post_u.dict()
#            post_1.remove(post)
#            post_1.append(post_update)
#            raise HTTPException(status_code=status.HTTP_201_CREATED,detail=post_update)
#         else:
#            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="doesnt exixt")

@app.get("/")
async def root():
    return {"message": "hello worlddddd"}