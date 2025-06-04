# Funções auxiliares como cálculo de odds
# utils/helpers.py

from config.config import TELEGRAM_TOKEN, GRUPO_FREE_ID, GRUPO_VIP_ID
from aiogram import Bot
import asyncio

async def enviar_para_grupos(texto):
    bot = Bot(token=TELEGRAM_TOKEN, parse_mode="MarkdownV2")
    errors = []
    sent = 0

    for group_id in [GRUPO_FREE_ID, GRUPO_VIP_ID]:
        if group_id is None or str(group_id).startswith("None") or int(group_id) == 0:
            continue
        try:
            await bot.send_message(chat_id=group_id, text=texto)
            sent += 1
            print(f"[BoyApostas] ✅ Mensagem enviada para grupo {group_id}")
        except Exception as e:
            errors.append(str(e))
            print(f"[BoyApostas] ❌ Erro ao enviar para grupo {group_id}: {e}")

    await bot.session.close()

    if not sent:
        print("[BoyApostas] Nenhuma mensagem enviada! Confira os IDs dos grupos no config.py")
    if errors:
        print("[BoyApostas] Alguns envios falharam: ", errors)
