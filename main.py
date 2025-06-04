# Arquivo principal do bot Boy Apostas
from aiogram import executor
from bot.handlers import dp
from scheduler.daily_tasks import start_scheduler
import asyncio

if __name__ == "__main__":
    start_scheduler()
    executor.start_polling(dp, skip_updates=True)