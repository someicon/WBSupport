import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram import types, Dispatcher, Bot

# from core.handlers.basic import router
# from core.handlers.preturn import router2
from handlers.user_private import user_private_router
from common.bot_cmds_list import private


load_dotenv()

ALLOWED_UPDATES = ["Message", "CallbackQuery"]


bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()

async def start_bot(bot: Bot):
    await bot.send_message(os.getenv("ADMIN_ID"), text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(os.getenv("ADMIN_ID"), text="Бот остановлен!")


async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    dp.include_routers(user_private_router)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # Эти методы для бота описаны в TelegramBot API
    await bot.delete_webhook(drop_pending_updates=True)

    # Добавление и удаление кнопки menu с командами
    #await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())

    try:
        await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
