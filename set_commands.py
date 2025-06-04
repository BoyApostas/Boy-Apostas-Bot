import asyncio
from aiogram import Bot, types
from config.config import TELEGRAM_TOKEN

async def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    
    commands = [
        types.BotCommand(command="start", description="Iniciar o bot"),
        types.BotCommand(command="ajuda", description="Ver comandos disponíveis"),
        types.BotCommand(command="free", description="Entrar no grupo gratuito"),
        types.BotCommand(command="vip", description="Ver informações do grupo VIP"),
    ]

    await bot.set_my_commands(commands)
    print("✅ Comandos definidos com sucesso!")

    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())