import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import time
import asyncio


api = "7308792898:AAGLeSCvR3DYGZDfR9weNSPDgsuN05b5Gtg"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def set_age(message):
    await message.answer("Привет! Я бот помогающий вашему здоровью.")
    await message.answer("Введите ваш возраст")
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age_now = message.text)
    data = await state.get_data()
    await message.answer("Введите ваш рост в сантиметрах")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth_now = message.text)
    data = await state.get_data()
    await message.answer("Введите ваш вес")
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight_now = message.text)
    data = await state.get_data()
    answer = (10 * int(data['age_now'])) + (6.25 * float(data['growth_now'])) - (5 * int(data['age_now'])) + 5
    await message.answer(f"Ваша норма {answer} калорий")
    await state.finish()




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)


