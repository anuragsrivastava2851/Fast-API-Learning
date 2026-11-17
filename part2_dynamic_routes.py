# dynamics routes and path parameters

from fastapi import FastAPI
app = FastAPI()
#user route 
@app.get("/users/{user_id}")  ## here user_id is a path parameter, it can be any integer value that is passed in the URL. For example, if the URL is /users/1, then user_id will be 1. If the URL is /users/2, then user_id will be 2.
def get_user(user_id: int): # user_id: int - means the user_id parameter must be an integer
    return {"user_id": user_id}


@app.get("/users/{user_name}")  
def get_user(user_name: str):
    return {"user_name": user_name}












#uvicorn main:app --reload