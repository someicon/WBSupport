import asyncio
from aiogram import Dispatcher, Bot, types

dp = Dispatcher()
bot = Bot(token="7358435330:AAEsvCM4sM1Qjluwu3AZJvmc_q44cbyndg4")


# Обработчик событий для бота. @dp.message() отлавливает все входящие сообщения
@dp.message()
async def echo(message: types.Message) -> None:
    await message.reply(text=f"Привет {message.chat.full_name}, это бот технический поддержки, чем я могу помочь ?")


async def start():
    # main() Начинает опрашивать сервера через диспетчер и передает обновления боту
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print('Бот выключен')
