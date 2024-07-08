from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

import core.keyboards.all_keyboards as kb


router = Router()


# Обработчик событий для бота. @dp.message() отлавливает все входящие сообщения
@router.message(CommandStart())
async def echo(message: Message) -> None:
    await message.answer(f"{message.chat.full_name} Добро пожаловать в чат!",
                         reply_markup=kb.main)


@router.message(F.text == "/help")
async def get_help(message: Message) -> None:
    await message.reply("Выберете пункт меню: ")


@router.message(F.text == "Позвонить")
async def get_phone(message: Message) -> None:
    await message.answer("Телефоны тех поддрежки : 1801, 1802, 1803, 1804")


# Обработчик для команды /start
@router.callback_query(F.data == "catalog")
async def get_catalog(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("Вы нажали кнопку Каталог",reply_markup= await kb.inline_items())
