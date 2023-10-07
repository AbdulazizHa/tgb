from aiogram import Router, types
from aiogram.filters import Command
from bot import scheduler, bot
from datetime import datetime
scheduler_router = Router

@scheduler_router.message(Command("remind"))
async def remind_me(message: types.Message):
    # scheduler.add_job(
    #     send_reminder,
    #     "interval",
    #     seconds=5,
    #     args=(message.from_user.id,)
    # )
    scheduler.add_job(
        send_reminder,
        "date",
        run_date=datetime(2023, 10, 9, 23, 00)
    )
    await message.answer("")

async def send_reminder(user_id: int):
    await bot.send_message(user_id, "Hi")