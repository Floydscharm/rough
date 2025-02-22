from typing import Optional, Union

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/") #decorator
def read_root():
    return {"message": "Hello World"}




#request get method url: "/"

@app.get("/posts")
def get_posts():
    return{"data": "this is your posts"}
@app.post("/createpost")
def create_post(new_post: Post):
    print(new_post.rating)
    return {"data": "new_post"}
# data we expect for a specific post request: title str, content str, category, Bool published