# Lida com comandos e interações do Telegram
from aiogram import Bot, Dispatcher, executor, types
from config.config import BOT_TOKEN, FREE_GROUP_ID, VIP_GROUP_ID
from bot.vip_manager import check_vip_status
from core.predictor import gerar_aposta_segura
from scheduler.check_results import verificar_resultados

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Bem-vindo ao Boy Apostas! Aguarde as próximas análises automáticas...")

@dp.message_handler(commands=["verificar_vip"])
async def verificar_vip(message: types.Message):
    status = check_vip_status(message.from_user.id)
    if status:
        await message.reply("✅ Você é VIP ativo!")
    else:
        await message.reply("❌ Você não está no grupo VIP ou seu plano expirou.")

@dp.message_handler(commands=["apostar"])
async def apostar(message: types.Message):
    aposta = gerar_aposta_segura()
    await message.reply(f"Aposta sugerida:\n\n{aposta}")

@dp.message_handler(commands=["verificar_resultado"])
async def resultado(message: types.Message):
    await verificar_resultados()

def start_bot():
    executor.start_polling(dp, skip_updates=True)
