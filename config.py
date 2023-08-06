from pydantic import BaseSettings

class settings(BaseSettings):
    dusername : str
    dpassword : str
    dhostname : str
    dport : int
    dname : str
    secret_key : str
    algorithm : str
    access_token_expire_minutes : int

    class Config:
        env_file = ".env"

setting = settings()