# Arquivo principal do bot Boy Apostas
import asyncio
import logging
from scheduler.daily_tasks import start_scheduler
from bot.handlers import dp, bot

async def main():
    logging.basicConfig(level=logging.INFO)
    start_scheduler()  # Inicia o agendador que roda as tarefas diárias (como as apostas às 07:00)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling()

if __name__ == "__main__":
    print("🚀 Iniciando Boy Apostas no Render (modo Background Worker)...")
    asyncio.run(main())