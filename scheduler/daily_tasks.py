# Agendamentos diários como envio às 07:00
import asyncio
from core.predictor import gerar_aposta_segura
from utils.helpers import enviar_para_grupos
from datetime import datetime

async def agendar_envio_apostas():
    while True:
        agora = datetime.now().strftime('%H:%M')
        if agora == "07:00":
            print("[Scheduler] Enviando aposta automática às 07:00...")
            await gerar_e_enviar()
            await asyncio.sleep(60)  # Evita enviar mais de uma vez no mesmo minuto
        await asyncio.sleep(20)  # Checa a cada 20 segundos

async def gerar_e_enviar():
    aposta = gerar_aposta_segura()
    if not aposta:
        print("[Aposta] Nenhuma aposta segura gerada.")
        return

    mensagem = f"🎯 *Aposta Gerada do Dia!*\n\n{aposta}\n\nBoa sorte, família! 🍀✅"

    with open("ultima_aposta.txt", "w") as f:
        f.write(aposta)

    await enviar_para_grupos(mensagem)

def start_scheduler():
    loop = asyncio.get_event_loop()
    loop.create_task(agendar_envio_apostas())