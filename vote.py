from multiprocessing import synchronize
import sys
from fastapi import  Depends, FastAPI, Response, status, HTTPException, APIRouter
import sys
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/models.py")
import models
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/post.py")
import post
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/user.py")
import user
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/schemas.py")
import schemas
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/oauth2.py")
import oauth2

from database import Sessionlocal
from database import get_db
router= APIRouter(prefix="/votes", tags=["votes"])
@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,  db:Sessionlocal=Depends(get_db), current_user:int=Depends(oauth2.get_current_user)):
    vote_query=db.query(models.vote_m).filter(models.vote_m.post_id==vote.post_id,models.vote_m.user_id==current_user.id)
    vota=vote_query.first()
    if vote.dir==1:
        if vota:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="you voted before!!!")
        elif not db.query(models.Post).filter(models.Post.id==vote.post_id).first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post does not exist!!!")
        else:
            new_vote=models.vote_m(post_id=vote.post_id, user_id=current_user.id)
            db.add(new_vote)
            db.commit()
            dd=db.query(models.vote_m).filter(models.vote_m.post_id==vote.post_id,models.vote_m.user_id==current_user.id).first()
        return{"vote":dd}

    else:
        if not vota:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="vote does not exist")
        else:
            vote_query.delete(synchronize_session=False)
            db.commit()
        return{"massage":"sussesfully deleted vote"}
