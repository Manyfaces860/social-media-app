from fastapi import HTTPException, APIRouter , status , Depends , Response
from sqlalchemy.orm import session
import utils , schemas, model , database , oauth2
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['authentication'])

@router.post('/login')
def login(login_cred : OAuth2PasswordRequestForm = Depends(), db : session = Depends(database.get_db)):
     
     user = db.query(model.User).filter(model.User.email == login_cred.username).first()
     
     if not user:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='invalid credentials')
     
     if not utils.verify(login_cred.password , user.password):
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail='invalid credentials')
     
     access_token = oauth2.create_access_token(data= {"user_id" : user.email})
     
     return {'token' : access_token , 'token_type': "Bearer"}