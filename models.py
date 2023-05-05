import sys
sys.path.insert(0, "C:/Users/Chalus System/PycharmProjects/fastapi39/app/database.py")
from database import Base
from sqlalchemy import TIMESTAMP, ForeignKey, Integer , String, Boolean, Column, Text
from typing import Text
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__="posts"
    id= Column(Integer, primary_key=True, nullable=False)
    title=Column(String,nullable=False )
    content=Column(String,nullable=False )
    published=Column(Boolean, server_default="true", nullable= False)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default= Text('now()'))
    owner_id= Column(Integer, ForeignKey("User.id", ondelete="CASCADE"), nullable=False)
    phone=Column(Integer,nullable=False )
    owner= relationship("users")
    phone=Column(String,nullable=False )


class users(Base):
    __tablename__="User"
    id= Column(Integer, nullable=False,primary_key=True)
    password=Column(String,nullable=False )
    Email= Column(String,nullable=False )
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default= Text('now()'))


class vote_m(Base):
    __tablename__="Votes"
    post_id=Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"),primary_key=True)
    user_id=Column(Integer, ForeignKey("User.id", ondelete="CASCADE"),primary_key=True)