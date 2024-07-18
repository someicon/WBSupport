import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from core.handlers.basic import router
from core.handlers.preturn import router2

load_dotenv()


bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()

async def start_bot(bot: Bot):
    await bot.send_message(os.getenv("ADMIN_ID"), text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(os.getenv("ADMIN_ID"), text="Бот остановлен!")


async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    dp.include_router(router=router)
    dp.include_router(router=router2)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
