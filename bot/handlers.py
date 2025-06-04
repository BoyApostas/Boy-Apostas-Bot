# Lida com comandos e interações do Telegram
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.config import TELEGRAM_TOKEN, PIX_KEY, GRUPO_FREE_LINK, GRUPO_VIP_LINK
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_TOKEN, parse_mode='Markdown')
dp = Dispatcher(bot)

# Teclado principal com comandos aprimorados
def get_main_menu():
    menu = InlineKeyboardMarkup(row_width=1)
    menu.add(
        InlineKeyboardButton("🔓 Entrar no Grupo Free", url=GRUPO_FREE_LINK),
        InlineKeyboardButton("💎 Acessar o Grupo VIP", callback_data="vip_info"),
        InlineKeyboardButton("📈 Ver Última Aposta Gerada", callback_data="ultima_aposta"),
        InlineKeyboardButton("ℹ️ Como Funciona", callback_data="info"),
        InlineKeyboardButton("❓ Ajuda", callback_data="help")
    )
    return menu

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
  text = (
    "👋 *Bem-vindo ao Boy Apostas!*\n\n"
    "📊 Sou um bot inteligente que analisa *estatísticas reais de jogos ao vivo* e monta apostas com *alta probabilidade de acerto* todos os dias!\n\n"
    "🚀 Veja como funciona:\n"
    "• Envio diário de *apostas seguras* com base em dados reais (odds entre 2.0 e 2.5)\n"
    "• Análise automática dos principais jogos do dia\n"
    "• Tudo 100% gratuito no nosso grupo Free\n\n"
    "💎 *Quer multiplicar seus ganhos?* No Grupo VIP você recebe:\n"
    "• Até *5 apostas ousadas por dia* com odds médias de *10.0*\n"
    "• Oportunidades ao vivo com alta chance de virada\n"
    "• Apostas bônus em caso de Red\n"
    "• Suporte prioritário e entrada antecipada\n\n"
    "🎯 *Segurança, transparência e resultados reais!*\n\n"
    "👇 Escolha abaixo por onde deseja começar:"
)

@dp.message_handler(commands=["free"])
async def grupo_free(message: types.Message):
    await message.answer(f"🔓 Clique para acessar o grupo Free:\n{GRUPO_FREE_LINK}")

@dp.message_handler(commands=["vip"])
async def grupo_vip(message: types.Message):
    await message.answer(
        f"💎 *Grupo VIP Exclusivo!*\n\n"
        "Com apenas *R$ 19,90/mês*, você recebe:\n"
        "- Até 5 apostas ousadas por dia com base em estatísticas ao vivo\n"
        "- Suporte personalizado\n"
        "- Entradas com odds de até *10.0*\n\n"
        f"📲 Chave Pix para pagamento: `{PIX_KEY}`\n\n"
        "Após o pagamento, envie o comprovante aqui. "
        "Um administrador irá liberar seu acesso ao grupo VIP manualmente.\n\n"
        "*Atenção: O acesso é individual e exclusivo para pagantes.*\n\n"
    )

@dp.callback_query_handler(lambda c: c.data == "vip_info")
async def info_vip(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(
        callback_query.from_user.id,
        f"💎 *Grupo VIP Exclusivo!*\n\n"
        "Com apenas *R$ 19,90/mês*, você recebe:\n"
        "- Até 5 apostas ousadas por dia com base em estatísticas ao vivo\n"
        "- Suporte personalizado\n"
        "- Entradas com odds de até *10.0*\n\n"
        f"📲 Chave Pix para pagamento: `{PIX_KEY}`\n\n"
        "Atenção: O acesso ao grupo VIP será liberado manualmente pelo administrador após o pagamento e validação do comprovante.\n\n"

    )

@dp.callback_query_handler(lambda c: c.data == "info")
async def btn_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(
        callback_query.from_user.id,
        "📊 *Como funciona o Boy Apostas?*\n\n"
        "- Analisamos estatísticas de jogos em tempo real\n"
        "- Geramos apostas com alta probabilidade de acerto\n"
        "- Enviamos automaticamente para os grupos\n"
        "- Você só precisa copiar e colar no site da sua escolha 🎯"
    )

@dp.callback_query_handler(lambda c: c.data == "help")
async def btn_help(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(
        callback_query.from_user.id,
        "📌 *Ajuda Rápida:*\n\n"
        "/start - Menu inicial\n"
        "/free - Link do grupo gratuito\n"
        "/vip - Como entrar no grupo VIP\n"
        "/ajuda - Ver comandos disponíveis"
    )

@dp.callback_query_handler(lambda c: c.data == "ultima_aposta")
async def btn_ultima(callback_query: types.CallbackQuery):
    try:
        with open("ultima_aposta.txt", "r") as f:
            aposta = f.read()
        await bot.send_message(callback_query.from_user.id, f"📢 *Última Aposta Gerada:*\n\n{aposta}")
    except:
        await bot.send_message(callback_query.from_user.id, "⚠️ Nenhuma aposta gerada ainda hoje.")


