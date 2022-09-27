from typing import Optional, Union
from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    id: UUID
    title: str
    body: str
    published: Optional[bool]


@app.get("/")
def helloWorld():
    return {"Hello": "World"}


@app.get("/api")
# this is how you use query params, you can set query to booleans
def my_first_function(limit, name):
    if name == 'diego':
        return {'data': {'name': f'{limit}diego'}, 'blogs': {'name': 'going out'}}
    else:
        return "does not equal that"


@app.get("/api/comment/{id}")
def get_comments_by_id(id: int):
    return {"data": {'id': id}}


@app.post("/api")
def creating_user(new_user: Blog):
    return f"new Blog was created with title as {new_user.title}"
