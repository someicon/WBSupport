from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import core.keyboards.all_keyboards as kb
from core.middlewares.middleware import TestMiddleware

router = Router()

router.message.middleware(TestMiddleware())


class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def echo(message: Message) -> None:
    await message.answer(f"{message.chat.full_name} Добро пожаловать в чат!")


@router.message(Command("list"))
async def get_list(message: Message):
    await message.answer(text="Список товаров", reply_markup=kb.main)


@router.callback_query(F.data == "catalog")
async def get_catalog(callback: CallbackQuery):
    await callback.message.edit_text("Каталог", reply_markup=kb.catalog)


@router.callback_query(F.data == "headphone")
async def get_main_menu(callback: CallbackQuery):
    await callback.message.edit_text("Наушники", reply_markup=kb.headphone)


@router.callback_query(F.data == "catalog_menu")
async def get_main_menu(callback: CallbackQuery):
    await callback.message.edit_text("Каталог", reply_markup=kb.catalog)


@router.callback_query(F.data == "main_menu")
async def get_main_menu(callback: CallbackQuery):
    await callback.message.edit_text("Главное меню", reply_markup=kb.main)


@router.message(Command("reg"))
async def reg_first(message: Message, state: FSMContext):
    await state.set_state(Reg.name)  # Установка состояния Регистрация.name
    await message.answer("Введите ваше имя")


@router.message(Reg.name)  # Фильтр отлавливает состояние Регистрация.name
async def reg_second(message: Message, state: FSMContext):
    # Сохранение введенной информации (Имя пользователя)
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)   # Смена состояния на Регистрация.number
    await message.answer("Введите ваш номер телефона")


@router.message(Reg.number)
async def reg_third(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    # data достает всю введенную информацию (хранится в словаре)
    data = await state.get_data()
    await message.answer(f"Регистрация завершена\nИмя: {data["name"]}\nНомер: {data["number"]}")
    await state.clear()  # Обязательная очистка состояния
