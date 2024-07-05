import asyncio
import os
from aiogram import Dispatcher, Bot, F,  types
from aiogram.filters import Command, CommandStart
from dotenv import load_dotenv

load_dotenv()

dp = Dispatcher()
bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))


# Обработчик событий для бота. @dp.message() отлавливает все входящие сообщения
@dp.message(CommandStart())
async def echo(message: types.Message) -> None:
    await message.answer(text=f"Тип чата {message.chat.id}\n"
                         f"@{message.chat.username}")


@dp.message((F.text == "/helpme") & (F.from_user.username == "some_icon"))
async def get_help(message: types.Message) -> None:
    await message.answer(f"{message.chat.full_name} Вы открыли окно помощи")


@dp.message(F.text.startswith("а"))
async def get_startwith(message: types.Message) -> None:
    await message.answer(f"{message.chat.first_name} Ваше сообщение начинается на букву А")


@dp.message(F.photo)
async def get_photo(message: types.Message) -> None:
    await message.answer(f"{message.chat.username} вы отправили фото")


async def start():
    # main() Начинает опрашивать сервера через диспетчер и передает обновления боту
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print("Бот выключен")
