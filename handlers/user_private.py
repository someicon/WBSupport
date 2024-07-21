from aiogram import types, Router, F
from aiogram.filters import Command, CommandStart


user_private_router = Router()

@user_private_router.message(Command("get_id"))
async def get_id(message: types.Message):
    await message.answer(f"Your id: {message.from_user.id}\n")
