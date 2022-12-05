from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content:str
    published:bool = True
    rating: Optional[int] = None

my_post=[{"title":"itle of post 1", "content":"content of post", "id":1},{"title":"favorite foods", "content":"i love pizza", "id":2}]

@app.get("/")
def root():
    return {"message": "welcome to the my api"}

@app.get("/posts")
def get_meth():
    return {"data":my_post}

@app.post("/posts")
def create_post(new_post: Post):
    post_dict=new_post.dict()
    post_dict['id']=randrange(0,100000)
    my_post.append(post_dict)
    return {"data":post_dict}
