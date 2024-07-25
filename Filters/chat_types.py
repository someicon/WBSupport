from typing import Any
from aiogram.filters import Filter
from aiogram import types


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types


    async def __call__(self, message: types.Message) -> Any:
        return message.chat.type in self.chat_types
