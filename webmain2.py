from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def main_page() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message": "Вы вошли как админ"}

#@app.get("/user/{username}/{id}")
#async def user_id(username: str = Path(min_length=3, max_length=15, discriminator="Введите ваше имя"),
#                  id: int = Path(ge=0, le=100, discriminator="Введите ваш номер")) -> dict:
#    return {"message": f"Вы вошли как пользователь № {username}:{id}"}

@app.get("/user/{userid}")
async def user_id(userid: Annotated[int, Path(ge=1, le=100, description="Enter your id", example="1")]) -> dict:
    return {"message": f"Вы вошли как пользователь № {userid}"}

@app.get("/user/{username}/{age}")
async def user_inf(username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
                   , age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}





