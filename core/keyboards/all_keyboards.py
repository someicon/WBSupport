from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data="catalog")],
    [InlineKeyboardButton(text="Корзина", callback_data="busket"),
     InlineKeyboardButton(text="Контакты", callback_data="contacts")],
])

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вешалки", callback_data="hanger")],
    [InlineKeyboardButton(text="Ковры", callback_data="carpet")],
    [InlineKeyboardButton(text="Наушники", callback_data="headphone")],
    [InlineKeyboardButton(text="На главную", callback_data="main_menu")]])


headphone = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="AirPods 3", callback_data="hanger")],
    [InlineKeyboardButton(text="AirPods Pro 2", callback_data="carpet")],
    [InlineKeyboardButton(text="AirPods Pro", callback_data="headphone")],
    [InlineKeyboardButton(text="Назад", callback_data="catalog_menu")],
    [InlineKeyboardButton(text="На главную", callback_data="main_menu")]])


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/watch?v=6i52YJqNziI"),
     InlineKeyboardButton(text="VK", url="https://www.youtube.com/watch?v=6i52YJqNziI")]])


help_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Позвонить"), KeyboardButton(text="Чат тех. поддрежки")]],
    resize_keyboard=True,
    input_field_placeholder="Выберете пункт меню")


# items = ["Вешалки", "Ковры", "Наушники"]
#
#
# async def inline_items():
#     keyboard = InlineKeyboardBuilder()
#     for item in items:
#         keyboard.add(InlineKeyboardButton(text=item,
#                                           url="https://www.youtube.com/watch?v=6i52YJqNziI"))
#     return keyboard.adjust(2).as_markup()
