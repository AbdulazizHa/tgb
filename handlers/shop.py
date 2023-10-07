from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from db.queries import get_products
from db.queries import get_products_by_category

shop_router = Router()

@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboards=[[
                KeyboardButton(text='Book'),
                KeyboardButton(text='Copybooks'),
        ],
            [
                KeyboardButton(text='Pens'),
                KeyboardButton(text='Pencils'),
            ],
            [KeyboardButton(
                text="Send your phone number",
                request_contact=True
            )],
            [KeyboardButton(
                text="Send your location",
                request_location=True
            )],
        ],
        resize_keyboard=True

    )
    for pr in get_products():
        await message.answer(pr[1])
    await message.answer("Choose category:", reply_markup=kb)

@shop_router.message(F.text == "Book")
async def show_book(message: types.Message):
    book = get_products_by_category(2)
    kb = ReplyKeyboardRemove()
    await message.answer("list of our books",
    reply_markup=kb)
    for m in book:
        await message.answer(m[1])