from sqlalchemy.orm import session
import  schemas
from fastapi import FastAPI , Response, status, HTTPException, Depends, APIRouter
from database import engine, get_db
import model , utils

router = APIRouter()

@router.post("/user" , status_code=status.HTTP_201_CREATED)
def user_create(user_cred : schemas.UserCreate ,db: session = Depends(get_db)):
    hashed_password = utils.hash(user_cred.password)
    user_cred.password = hashed_password
    user = model.User(**user_cred.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"data": user}