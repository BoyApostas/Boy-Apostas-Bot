# Arquivo principal do bot Boy Apostas
from bot.handlers import dp, bot
from aiogram import executor
from scheduler.daily_tasks import schedule_daily_tasks
from scheduler.check_results import schedule_result_check

def main():
    print("Iniciando o bot Boy Apostas...")
    start_bot()
    schedule_daily_tasks()
    schedule_result_check()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

