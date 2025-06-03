# Agendamentos diários como envio às 07:00
import asyncio
from datetime import datetime, timedelta
from aiogram import Bot
from core.predictor import gerar_aposta_segura
from config.config import BOT_TOKEN, FREE_GROUP_ID, DAILY_POST_HOUR, DAILY_POST_MINUTE

bot = Bot(token=BOT_TOKEN)

async def enviar_aposta_diaria():
    aposta = gerar_aposta_segura()
    try:
        await bot.send_message(FREE_GROUP_ID, aposta)
    except Exception as e:
        print(f"Erro ao enviar aposta diária: {e}")

def schedule_daily_tasks():
    asyncio.create_task(agendar_envio_diario())

async def agendar_envio_diario():
    while True:
        agora = datetime.now()
        proximo_envio = agora.replace(hour=DAILY_POST_HOUR, minute=DAILY_POST_MINUTE, second=0, microsecond=0)

        if proximo_envio <= agora:
            proximo_envio += timedelta(days=1)

        tempo_espera = (proximo_envio - agora).total_seconds()
        await asyncio.sleep(tempo_espera)
        await enviar_aposta_diaria()
