from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import core.keyboards.all_keyboards as kb


router = Router()


# Обработчик событий для бота. @dp.message() отлавливает все входящие сообщения
@router.message(CommandStart())
async def echo(message: Message) -> None:
    await message.answer(f"{message.chat.full_name} Добро пожаловать в чат!",
                         reply_markup=await kb.inline_items())


@router.message((F.text == "/help") & (F.from_user.username == "some_icon"))
async def get_help(message: Message) -> None:
    await message.answer(f"{message.chat.full_name} Вы открыли окно помощи")


@router.message(F.text.startswith("а"))
async def get_startwith(message: Message) -> None:
    await message.answer(f"{message.chat.first_name} Ваше сообщение начинается на букву А")


@router.message(F.photo)
async def get_photo(message: Message) -> None:
    await message.answer(f"ID фото: {message.photo[-1].file_id}")
