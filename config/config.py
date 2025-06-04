# Token do Bot Telegram
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = "8056306367:AAEyaeX-lToKYDN-LIkgn-O6-em-OdtB84c"
BOT_TOKEN = TELEGRAM_TOKEN  
PIX_KEY = "boyapostaspix@gmail.com"

# Links dos grupos
GRUPO_FREE_LINK = "https://t.me/+hBaBOF7qSVw0ZGUx"
GRUPO_VIP_LINK = "https://t.me/+1Deb4RL0C5lkNzEx"

# ID dos grupos 
FREE_GROUP_ID = int(os.getenv("FREE_GROUP_ID", "-1000000000000"))
VIP_GROUP_ID = int(os.getenv("VIP_GROUP_ID", "-1000000000000"))

# Preço do VIP
VIP_PRECO = 19.90

# Nome do projeto
NOME_PROJETO = "Boy Apostas"

# Mensagens fixas
MENSAGEM_BOAS_VINDAS = (
    "👋 *Bem-vindo ao Boy Apostas!*\n\n"
    "Sou um bot automático que analisa os jogos mais importantes do dia e gera apostas com *alta probabilidade de acerto*.\n\n"
    "🆓 Apostas gratuitas no Grupo Free\n"
    "💎 Apostas ousadas no Grupo VIP com *odds médias de 10*!"
)

MENSAGEM_VIP = (
    "💎 *Acesso ao Grupo VIP:*\n\n"
    "Com apenas *R$ 19,90/mês*, você recebe:\n"
    "- Até 5 apostas ousadas por dia com base em estatísticas ao vivo\n"
    "- Suporte personalizado\n"
    "- Entradas com odds de até *10.0*\n\n"
    f"📲 Chave Pix para pagamento:\n`{PIX_KEY}`\n\n"
    "Após o pagamento, envie o comprovante aqui e você será liberado automaticamente no VIP!\n"
    f"Grupo VIP: {GRUPO_VIP_LINK}"
)

# Configuração da API-Football
API_FOOTBALL_KEY = "0e25118fbcmsha55117055c74d7fp12b621jsnac9d871ee693"

# Horários e lembretes
HORARIO_ENVIO_APOSTAS = "07:00"
HORARIO_LEMBRETE_PAGAMENTO = ["2d", "1d", "0d"]

# Arquivo local para registrar última aposta
ARQUIVO_ULTIMA_APOSTA = "ultima_aposta.txt"