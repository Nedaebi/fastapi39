from fastapi import APIRouter, Depends, FastAPI, Response, status, HTTPException
import sys

from sqlalchemy import func
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/schemas.py")
import schemas
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/models.py")
import models
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/database.py")
import database
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/oauth2.py")
import oauth2
from database import get_db
from database import Sessionlocal
from typing import List, Optional


router= APIRouter(prefix="/posts",tags=["posts"])
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
async def create_posts(post:schemas.BPost,db:Sessionlocal=Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    #   cursor.execute("""INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING *""",(post.title, post.content))
    #   new_post= cursor.fetchone()
    #   conn.commit()
      new_post= models.Post(owner_id= current_user.id,**post.dict())
      db.add(new_post)
      db.commit()
      db.refresh(new_post)
      return new_post
#     post_1.append(post.dict())
#     print(post.dict())
#     raise HTTPException(status_code=status.HTTP_201_CREATED, detail=post.dict())

# @router.get("/",response_model=List[schemas.Post])
@router.get("/",response_model=List[schemas.postout])
# async def posts(post:Post):
def get_posts(db:Sessionlocal=Depends(get_db),current_user=Depends(oauth2.get_current_user),limit:int=10,skip:int=0,search:Optional[str]=""):
    #    cursor.execute("""SELECT * FROM posts""")
    #    posts= cursor.fetchall()
    # posts= db.query(models.Post).filter(models.Post.owner_id==current_user.id, models.Post.title.contains(search)).limit(limit).offset(skip).all()
    results= db.query(models.Post, func.count(models.vote_m.post_id).label("votes_m")).join(models.vote_m, models.vote_m.post_id==models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    #  return posts
    return results



@router.get("/{id}",response_model=schemas.postout)
async def posts(id:int,db:Sessionlocal=Depends(get_db),current_user=Depends(oauth2.get_current_user)):
# def get_posts(db:Sessionlocal=Depends(get_db), ):
    # cursor.execute("""SELECT * FROM posts WHERE id=%s""",(str(id),))
    # post= cursor.fetchone()
    # print(post)
    # post= db.query(models.Post).filter(models.Post.id==id).first()
   
    post=  db.query(models.Post, func.count(models.vote_m.post_id).label("votes_m")).join(models.vote_m, models.vote_m.post_id==models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    print(models.Post.owner_id)
    print(current_user.id)
    if not post :
         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post number {id} does not exist")
    elif  not models.Post.owner_id!=current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "post is not yours")
    return post

    # for post in post_1:
    #     if post["rating"]==id:
        #     return{"data":post}
        # else:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="doesnt exixt")
        #     return{"warning":"doesnt exist"}

@router.delete("/{id}")
async def posts(id:int,db:Sessionlocal=Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    #    cursor.execute("""DELETE FROM posts WHERE id=%s RETURNING * """,(str(id),))
    #    post_deleted= cursor.fetchone()
       post= db.query(models.Post).filter(models.Post.id==id)
       if post.first()==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="doesnt exixt")
       elif  not post.first().owner_id==current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "post is not yours")
       else:
           post.delete(synchronize_session=False)
    #    conn.commit()
           db.commit()
       return Response(status_code=status.HTTP_204_NO_CONTENT)


#     for post in post_1:
#         if post["rating"]==id:
#            post_1.remove(post)
#            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
#         else:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="doesnt exixt")

@router.put("/{id}")
async def update_post(id:int, post:schemas.BPost,db:Sessionlocal=Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    #  cursor.execute(""" UPDATE posts SET title=%s, content=%s WHERE id=%s RETURNING * """,(post.title,post.content, str(id),))
    #  post_updated= cursor.fetchone()
     post_updated=db.query(models.Post).filter(models.Post.id==id)
     if post_updated.first()==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=" post doesnt exixt")
     elif  not post_updated.first().owner_id==current_user.id:
         raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "post is not yours")
    #  conn.commit()
     else:
         post_updated.update(post.dict(), synchronize_session=False)
         db.commit()
     return{"data":"successfully updated"}