from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import core.keyboards.all_keyboards as kb
from core.middlewares.middleware import TestMiddleware

router = Router()

class TextAnswer(StatesGroup):
    text = State()


@router.message(Command("help"))
async def echo(message: Message, state: FSMContext) -> None:
    await state.set_state(TextAnswer.text)
    await message.answer("Отправьте любое сообщение")


@router.message(TextAnswer.text)
async def send_echo(message: Message, state: FSMContext) -> None:
    await state.update_data(text=message.text)
    data = await state.get_data()
    await message.answer(f"Ваше сообщение:\n{data["text"]}")
    await state.clear()
