from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data="catalog")],
    [InlineKeyboardButton(text="Корзина", callback_data="busket"),
     InlineKeyboardButton(text="Контакты", callback_data="contacts")],
    [InlineKeyboardButton(text="Возврат товара",
                          callback_data="p_return")]
])

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вешалки", callback_data="hanger")],
    [InlineKeyboardButton(text="Ковры", callback_data="carpet")],
    [InlineKeyboardButton(text="Наушники", callback_data="headphone")],
    [InlineKeyboardButton(text="На главную", callback_data="main_menu")]])


headphone = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="AirPods 3", url="https://support.apple.com/ru-ru/111863")],
    [InlineKeyboardButton(text="AirPods Pro 2",
                          url="https://re-store.ru/catalog/MTJV3/")],
    [InlineKeyboardButton(text="AirPods Pro", url="https://clck.ru/3BoqY5")],
    [InlineKeyboardButton(text="Назад", callback_data="catalog_menu")],
    [InlineKeyboardButton(text="На главную", callback_data="main_menu")]])


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/watch?v=6i52YJqNziI"),
     InlineKeyboardButton(text="VK", url="https://www.youtube.com/watch?v=6i52YJqNziI")]])


help_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Позвонить"), KeyboardButton(text="Чат тех. поддрежки")]],
    resize_keyboard=True,
    input_field_placeholder="Выберете пункт меню")

reason_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Не подошел размер",
        callback_data="reason_1")],
    [InlineKeyboardButton(
        text="Не соответствует описанию/фото",
        callback_data="reason_2")],
    [InlineKeyboardButton(
        text="Низкое качество изготовления",
        callback_data="reason_3")],
    [InlineKeyboardButton(
        text="Брак",
        callback_data="reason_4")],
    [InlineKeyboardButton(
        text="Не подошел фасон, посадка, стиль",
        callback_data="reason_5")],
    [InlineKeyboardButton(
        text="Доставлен не тот товар",
        callback_data="reason_6")],
    [InlineKeyboardButton(
        text="Товар не был доставлен",
        callback_data="reason_7")],
    [InlineKeyboardButton(
        text="Другое",
        callback_data="reason_8")]
])

point_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Пункт выдачи Москва",
        callback_data="point_1")],
    [InlineKeyboardButton(
        text="Пункт выдачи Санкт-Петербург",
        callback_data="point_2")],
    [InlineKeyboardButton(
        text="Пункт выдачи Казань",
        callback_data="point_3")]
])

# items = ["Вешалки", "Ковры", "Наушники"]
#
#
# async def inline_items():
#     keyboard = InlineKeyboardBuilder()
#     for item in items:
#         keyboard.add(InlineKeyboardButton(text=item,
#                                           url="https://www.youtube.com/watch?v=6i52YJqNziI"))
#     return keyboard.adjust(2).as_markup()
