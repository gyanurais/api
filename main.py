from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

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
    return {"data":"ṭhis is for recieve the data"}

@app.post("/createpost")
def create_post(new_post: Post):
    # print(new_post)
    # print(new_post.dict())
    my_post.append(new_post.dict())
    return {"data":new_post}