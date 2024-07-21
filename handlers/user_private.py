from aiogram import types, Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(f"Добрый день {message.from_user.full_name}. Добро пожаловать в чат")

@user_private_router.message(Command("menu"))
async def menu_cmd(message: Message):
    await message.answer("Меню: ")


@user_private_router.message(Command("about"))
async def about_cmd(message: Message):
    await message.answer("О нас: ")


@user_private_router.message(Command("payment"))
async def payment_cmd(message: Message):
    await message.answer("Способы оплаты: ")


@user_private_router.message(Command("shipping"))
async def shipping_cmd(message: Message):
    await message.answer("Варианты доставки: ")


@user_private_router.message(Command("get_id"))
async def get_id(message: types.Message):
    await message.answer(f"{message.from_user.full_name}\nYour id: {message.from_user.id}\n")
