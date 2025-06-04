# Arquivo principal do bot Boy Apostas
from aiogram import executor
from bot.handlers import dp
from scheduler.daily_tasks import start_scheduler
import threading

def iniciar_scheduler_em_thread():
    thread = threading.Thread(target=start_scheduler)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    iniciar_scheduler_em_thread()
    executor.start_polling(dp, skip_updates=True)
