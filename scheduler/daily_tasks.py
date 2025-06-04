# Agendamentos diários como envio às 07:00
import schedule
import time
import asyncio
from core.predictor import gerar_aposta_segura
from utils.helpers import enviar_para_grupos
import logging

logging.basicConfig(level=logging.INFO)

def schedule_daily_tasks():
    schedule.every().day.at("07:00").do(lambda: asyncio.run(gerar_e_enviar()))
    logging.info("📅 Tarefa agendada para 07:00 da manhã, todos os dias.")

async def gerar_e_enviar():
    logging.info("🚀 Iniciando geração da aposta segura...")
    aposta = gerar_aposta_segura()

    if aposta:
        mensagem = f"🎯 *Aposta Gerada do Dia!*\n\n{aposta}\n\nBoa sorte, família! 🍀✅"
        try:
            with open("ultima_aposta.txt", "w") as f:
                f.write(aposta)
            await enviar_para_grupos(mensagem)
            logging.info("✅ Aposta enviada com sucesso para os grupos.")
        except Exception as e:
            logging.error(f"❌ Erro ao enviar aposta: {e}")
    else:
        logging.warning("⚠️ Nenhuma aposta foi gerada hoje. Nenhuma entrada enviada.")

def start_scheduler():
    schedule_daily_tasks()
    while True:
        schedule.run_pending()
        time.sleep(60)  # Verifica a cada minuto