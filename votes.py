from sqlalchemy.orm import session
import  schemas
from fastapi import status, HTTPException, Depends , APIRouter
import model
from database import get_db
import oauth2

router = APIRouter()

@router.post("/vote", status_code=status.HTTP_201_CREATED )
def vote(vote: schemas.Vote, db: session = Depends(get_db) , user_id: str = Depends(oauth2.get_current_user)):
    
    find_post = db.query(model.Vote).filter(model.Vote.post_id == vote.post_id).first()

    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'post does not exist')

    vote_query = db.query(model.Vote).filter(model.Vote.post_id == vote.post_id , model.Vote.users_email == user_id)
    found_vote = vote_query.first()

    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail=f'{user_id} has already voted on {vote.post_id}')
        
        add_vote = model.Vote(post_id = vote.post_id, users_email = user_id)
        db.add(add_vote)
        db.commit()
        return {"message" : "successfully added vote"}
    
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message" : "successfully deleted vote"}