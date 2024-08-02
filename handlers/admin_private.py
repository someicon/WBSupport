from aiogram import F, Router, types
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter, IsAdmin
from keyboards.reply import get_keyboard

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private'], IsAdmin()))
