import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv

load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
     await message.reply("Hello")

@dp.message(Command("photo"))
async def send_photo(message: types.Message):
    with open(random.choices("image", "rb")) as photo:
        await message.answer_photo(photo)


@dp.message(Command("info"))
async def info(message: types.Message):
    await message.answer(f"your id={message.from_user.id}, your first name={message.from_user.first_name}, your nickname={message.from_user.username}")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
