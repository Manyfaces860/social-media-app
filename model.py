from sqlalchemy.sql.expression import null, text
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Boolean, String, TIMESTAMP , ForeignKey
from database import base 


class Post(base):
    __tablename__ = "posts"
    
    id = Column(Integer , primary_key= True , nullable= False)
    title = Column(String, nullable= False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
    owner_id = Column(String , ForeignKey("users.email", ondelete='CASCADE'), nullable=False)
    # owner = relationship('User')
    
class User(base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key= True , nullable= False)
    email = Column(String , unique=True , nullable = False)
    password = Column(String , nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
    
class Vote(base):
    __tablename__ = "votes"

    post_id = Column(Integer , ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    users_email = Column(String , ForeignKey("users.email", ondelete="CASCADE"), primary_key=True)