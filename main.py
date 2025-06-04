# Arquivo principal do bot Boy Apostas
import threading
from aiogram import executor
from bot.handlers import dp
from scheduler.daily_tasks import start_scheduler

def iniciar_scheduler_em_thread():
    thread = threading.Thread(target=start_scheduler, name="AgendadorDeApostas")
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    print("🔄 Iniciando bot Boy Apostas...")
    iniciar_scheduler_em_thread()
    executor.start_polling(dp, skip_updates=True)