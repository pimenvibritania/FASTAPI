from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello jancuk"}

@app.get("/test")
def root():
    return {"message": "Hello test"}

@app.post("/post")
def createPost(post: Post):
    return {"data": post}
    