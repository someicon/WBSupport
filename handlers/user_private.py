from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter
from keyboards import reply


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


# @user_private_router.message(CommandStart())
# async def start_cmd(message: Message):
#     await message.answer(f"Добрый день {message.from_user.full_name}. Добро пожаловать в чат",
#                          reply_markup=reply.start_kb2.as_markup(
#                              resize_keyboard=True,
#                              input_field_placeholder="Start"
#     ))


# @user_private_router.message(CommandStart())
# async def start_cmd(message: Message):
#     await message.answer(f"Добрый день {message.from_user.full_name}. Добро пожаловать в чат",
#                          reply_markup=reply.start_kb)

@user_private_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(
        "Привет, добро пожаловать в чат",
        reply_markup=reply.get_keyboard(
            "Меню",
            "О магазине",
            "Варианты оплаты",
            "Варианты доставки",
            "Отправить номер телефона",
            placeholder="Что вас интересует ?",
            request_contact=4,
            size=(2, 2, 1)
        )
    )



@user_private_router.message(F.text.lower() == "меню")
async def menu_cmd(message: Message):
    await message.answer("<i>Меню:</i>", reply_markup=reply.remove_kb)


@user_private_router.message(F.text.lower() == "о нас")
@user_private_router.message(Command("about"))
async def about_cmd(message: Message):
    await message.answer("<i>О нас: </i>")


@user_private_router.message(F.text.lower() == "способы оплаты")
@user_private_router.message(Command("payment"))
async def payment_cmd(message: Message):
    text = as_marked_section(
        Bold("Способы оплаты:"),
        "Картой онлайн",
        "Картой/наличными при получении",
        "В приложении вашего банка через СБП",
        marker="✅ "
    )
    await message.answer(text.as_html())


@user_private_router.message(F.text.lower() == "варианты доставки")
@user_private_router.message(Command("shipping"))
async def shipping_cmd(message: Message):
    text = as_list(
        as_marked_section(
            Bold("Варианты доставки"),
            "Почта",
            "Курьер по городу",
            "СДЕК",
            marker="✅ "
        ),
        as_marked_section(
            Bold("Время доставки: "),
            "Доставка осуществляется в будние дни с 10:00 до 23:00",
            marker="🚙",
        ),
        sep=f"\n{"-" * 100}\n"
    )
    await message.answer(text.as_html())


@user_private_router.message(Command("get_id"))
async def get_id(message: types.Message):
    await message.answer(f"{message.from_user.full_name}\nYour id: {message.from_user.id}\n")


@user_private_router.message(Command("info"))
async def get_info(message: types.Message):
    await message.answer(text="Выберете пункт меню", reply_markup=reply.test_kb)


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer("Контакт получен")
    await message.answer(message.contact)


@user_private_router.message(F.location)
async def get_contact(message: types.Message):
    await message.answer("Локация получена")
    await message.answer(message.location)
