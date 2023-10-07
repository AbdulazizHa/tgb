import asyncio
from handlers import start_router, echo_router, shop_router, questions_router, scheduler_router
import logging
from bot import bot, dp, scheduler
from aiogram.types import BotCommand
from db.queries import init_db, create_tables, populate_tables

async def on_startup(_):
    init_db()
    create_tables()
    populate_tables()
async def main():
    await bot.set_my_commands(
        BotCommand(command="start", description="Start Bot"),
        BotCommand(command="info", description="information"),
        BotCommand(command="shop", description="Book shop"),
        BotCommand(command="photo", description="Random photo"),
    )

    dp.startup.register(on_startup)

    dp.include_router(start_router)
    dp.include_router(echo_router)
    dp.include_router(shop_router)
    dp.include_router(scheduler_router)

    scheduler.start()
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())



