from fastapi import FastAPI, status, Body, HTTPException, Path
from pydantic import BaseModel
from typing import List
from typing import Annotated

app = FastAPI()

Users = []

class User(BaseModel):
    id: int = None
    username: str = None
    age: int = None


@app.get("/")
async def welcome_for_users() -> str:
    return "Welcome"


@app.get("/users")
async def get_all_users() -> List[User]:
    return Users


@app.get(path="/users/{user_id}")
def get_user(user_id: int) -> User:
    try:
        return Users[user_id]
    except:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")



@app.post("/user/{username}/{age}")
async def create_user(user: User) -> str:
    user.id = len(Users)+1
    Users.append(user)
    return f"The user {len(Users)} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: int, user: User) -> str:
    try:
        edit_user = Users[user_id]
        user.id = user_id
        edit_user.username = user
        return f"The user {user_id} is updated"
    except:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")


@app.delete("/user/{user_id}")
async def delete_message(user_id: int) -> str:
    try:
        Users.pop(user_id)
        return f"User with {user_id} was deleted"
    except:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")


