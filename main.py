from typing import Union

from fastapi import FastAPI

app = FastAPI()


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
