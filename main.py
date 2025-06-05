# Arquivo principal do bot Boy Apostas
import asyncio
import logging
from scheduler.daily_tasks import start_scheduler

logging.basicConfig(level=logging.INFO)

async def main():
    logging.info("🚀 Iniciando Boy Apostas no Render (modo Background Worker)...")
    start_scheduler()

if __name__ == "__main__":
    asyncio.run(main())