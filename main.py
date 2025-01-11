import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

bot = Bot("7787591480:AAHEZLQ-Z_X89dr9byD3eXeWcQFNYH99jMw")
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
