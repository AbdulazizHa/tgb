from aiogram import types, Router, F
from aiogram.filters import Command
from text import START_TEXT, ABOUT_US
import random
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                IButton(text="Our site: ", url="https://geeks.com"),
                IButton(text="Our Instagram: ", url="https://instagram/lgeeks.com")
            ],
            [
                IButton(text="About Us : ", callback_data="about")
            ]
        ]
    )
    await message.reply(START_TEXT)

@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.message.answer(ABOUT_US)

@start_router.message(Command("photo"))
async def send_photo(message: types.Message):
    with open(random.choices("image", "rb")) as photo:
        await message.answer_photo(photo)


@start_router.message(Command("info"))
async def info(message: types.Message):
    await message.answer(f"your id={message.from_user.id}, your first name={message.from_user.first_name}, your nickname={message.from_user.username}")

@start_router.message()
async def echo(message: types.Message):
    await message.answer(message.text)
