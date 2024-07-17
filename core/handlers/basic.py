from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import core.keyboards.all_keyboards as kb
from core.middlewares.middleware import TestMiddleware

router = Router()

