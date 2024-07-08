from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог")],
    [KeyboardButton(text="Корзина"), KeyboardButton(text="Контакты")]],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню")

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/watch?v=6i52YJqNziI"),
     InlineKeyboardButton(text="VK", url="https://www.youtube.com/watch?v=6i52YJqNziI")]])

items = ["Вешалки", "Ковры", "Наушники"]


async def inline_items():
    keyboard = InlineKeyboardBuilder()
    for item in items:
        keyboard.add(InlineKeyboardButton(text=item,
                                          url="https://www.youtube.com/watch?v=6i52YJqNziI"))
    return keyboard.adjust(2).as_markup()
