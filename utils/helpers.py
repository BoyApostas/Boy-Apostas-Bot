# Funções auxiliares como cálculo de odds
# utils/helpers.py

from config.config import TELEGRAM_TOKEN, GRUPO_FREE_ID, GRUPO_VIP_ID
from aiogram import Bot

bot = Bot(token=TELEGRAM_TOKEN)

async def enviar_para_grupos(texto):
    try:
        await bot.send_message(chat_id=GRUPO_FREE_ID, text=texto)
    except Exception as e:
        print(f"[Erro] ao enviar para grupo free: {e}")
    try:
        await bot.send_message(chat_id=GRUPO_VIP_ID, text=texto)
    except Exception as e:
        print(f"[Erro] ao enviar para grupo vip: {e}")
