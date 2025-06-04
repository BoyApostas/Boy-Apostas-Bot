# Agendamentos diários como envio às 07:00
import schedule
import time
import asyncio
from core.predictor import gerar_aposta_segura
from utils.helpers import enviar_para_grupos

def schedule_daily_tasks():
    schedule.every().day.at("07:00").do(lambda: asyncio.run(gerar_e_enviar()))

async def gerar_e_enviar():
    print("⏰ Gerando aposta automática...")
    aposta = gerar_aposta_segura()
    mensagem = f"🎯 *Aposta Gerada do Dia!*\n\n{aposta}\n\nBoa sorte, família! 🍀✅"

    with open("ultima_aposta.txt", "w") as f:
        f.write(aposta)

    await enviar_para_grupos(mensagem)
    print("✅ Aposta enviada para os grupos!")

def start_scheduler():
    print("🔔 Scheduler de apostas iniciado (daily_tasks.py)")
    schedule_daily_tasks()
    while True:
        schedule.run_pending()
        time.sleep(1)
