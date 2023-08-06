from jose import JWTError , jwt 
import datetime
import schemas
from fastapi import Depends , status , HTTPException
from fastapi.security import OAuth2PasswordBearer 
from config import setting

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

# secret_key = "b48c9d5457366ea296afb3190d6290875b508017ba04bcb56fe6c57123fe519"
# algorithm = "HS256"
# access_token_expire_minutes = 30

secret_key = setting.secret_key
algorithm = setting.algorithm
access_token_expire_minutes = setting.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=access_token_expire_minutes)
    to_encode.update({'exp': expire})
    
    encoded_jwt = jwt.encode(to_encode , secret_key , algorithm= algorithm)
    
    return encoded_jwt 

def verify_access_token(token : str , credentials_exception):
    try: 
        payload = jwt.decode(token , secret_key, algorithms=[algorithm])
        
        id : str = payload.get("user_id")
        
        if id is None:
            raise credentials_exception
        token_data = schemas.Tokendata(id=id)
        
    except JWTError:
        raise credentials_exception
    
    return token_data.id
    
def get_current_user(token:str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail=f'could not validate credentials', headers= {'www-authencate': 'Bearer'})
    
    return verify_access_token(credentials_exception=credentials_exception , token=token)
    