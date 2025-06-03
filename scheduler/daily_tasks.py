# Agendamentos diários como envio às 07:00
import asyncio
from core.predictor import gerar_aposta_segura
from utils.helpers import enviar_para_grupos
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

async def executar_rotina_diaria():
    try:
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        logging.info(f"⏰ Iniciando rotina de apostas: {agora}")

        texto_espera = (
            "🎯 *Apostas do Dia em Análise...*
\n"
            "Nosso sistema está analisando milhares de dados dos principais campeonatos ao redor do mundo
"
            "para encontrar combinações com maior chance de acerto!")
        await enviar_para_grupos(texto_espera)

        aposta_gerada = await gerar_aposta_segura()

        if aposta_gerada:
            texto_aposta = (
                "✅ *Aposta Segura do Dia!*
\n"
                f"📅 *Data:* {datetime.now().strftime('%d/%m/%Y')}
"
                f"📈 *Odd Total:* {aposta_gerada['odd_total']}
"
                "\n\n*Jogos Selecionados:*\n"
            )
            for jogo in aposta_gerada['jogos']:
                texto_aposta += f"⚽ {jogo['time']} - Odd {jogo['odd']}
"

            texto_aposta += (
                "\n🔍 Análise completa feita com base em desempenho recente, estatísticas ao vivo e comportamento de mercado.
"
                "🚀 Recomendamos apostar até 1 hora antes do primeiro jogo!")

            await enviar_para_grupos(texto_aposta)
        else:
            await enviar_para_grupos("⚠️ Nenhuma aposta segura foi gerada hoje. O sistema não encontrou combinações confiáveis o suficiente para garantir segurança. Amanhã tem mais!")

    except Exception as e:
        logging.error(f"Erro na rotina diária: {e}")
        await enviar_para_grupos("❌ Ocorreu um erro durante a geração das apostas de hoje. Equipe técnica foi notificada.")

if __name__ == "__main__":
    asyncio.run(executar_rotina_diaria())
