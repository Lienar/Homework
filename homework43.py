import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import time
import asyncio


api = "7308792898:AAGLeSCvR3DYGZDfR9weNSPDgsuN05b5Gtg"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(commands=['start'])
async def all_message(message):
    print ("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Hello!")

@dp.message_handler()
async def all_message(message):
    print ("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)

