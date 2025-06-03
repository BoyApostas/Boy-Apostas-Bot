# Verifica se apostas bateram (Green/Red)
import asyncio
from aiogram import Bot
from config.config import BOT_TOKEN, FREE_GROUP_ID
from datetime import datetime
from core.predictor import gerar_aposta_segura

bot = Bot(token=BOT_TOKEN)

# Simulação simples para teste
ultimos_resultados = {"bateu": True}  # Trocar depois por verificação real da API

async def verificar_resultados():
    if ultimos_resultados.get("bateu"):
        await bot.send_message(FREE_GROUP_ID, "✅ Deu Green Família ✅✅✅")
    else:
        await bot.send_message(FREE_GROUP_ID, "❌ Deu Red ❌")
        await enviar_aposta_recuperacao()

async def enviar_aposta_recuperacao():
    aposta = gerar_aposta_segura()
    msg = (
        "🎯 Aposta adicional bônus!\n"
        "Tentativa de recuperar a perda anterior.\n"
        "⚠️ Esta aposta tem odd mais alta e envolve mais risco.\n\n"
        f"{aposta.replace('Odd estimada: 2.5', 'Odd estimada: 4.0')}"
    )
    await bot.send_message(FREE_GROUP_ID, msg)

def schedule_result_check():
    asyncio.create_task(agendar_verificacao())

async def agendar_verificacao():
    while True:
        agora = datetime.now()
        if agora.hour == 21:  # Verificação todo dia às 21h
            await verificar_resultados()
        await asyncio.sleep(3600)  # Checa a cada hora
