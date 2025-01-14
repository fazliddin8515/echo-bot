import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"salom, {message.from_user.first_name}")

@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

async def main():
    print("bot has been started...")
    await dp.start_polling(bot)

asyncio.run(main())
