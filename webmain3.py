from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": ["Имя: Example", "возраст: 18"]}


@app.get("/")
async def welcome_for_users() -> str:
    return "Welcome"


@app.get("/users")
async def get_all_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = [f"Имя: {username}", f"возраст: {age}"]
    return f"The user {current_index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: str, username: str, age: int) -> str:
    users[user_id] = [f"Имя: {username}", f"возраст: {age}"]
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_message(user_id: str) -> str:
    users.pop(user_id)
    return f"User with {user_id} was deleted"


