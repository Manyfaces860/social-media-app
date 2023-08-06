from fastapi import FastAPI , Depends
from sqlalchemy.orm import session
import model
from database import engine, get_db
import posts
import users , oauth
import votes
from fastapi.middleware.cors import CORSMiddleware

model.base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"data": "good"}

@app.get("/sqlalchemy")
def test(db: session = Depends(get_db)):
    post = db.query(model.Post).all()
    # print(post)
    return {"data":post}

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(oauth.router) 
app.include_router(votes.router) 

# 8:07:33 is the stopping point where we will implement foreign keys. (done)