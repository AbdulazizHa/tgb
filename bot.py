from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from os import getenv
from  apscheduler.schedulers.asyncio import  AsyncIOScheduler

load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
scheduler = AsyncIOScheduler()
