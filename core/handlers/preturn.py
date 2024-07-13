from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import core.keyboards.all_keyboards as kb

router2 = Router()


class PurchaseReturn(StatesGroup):
    reason = State()
    point = State()


@router2.callback_query(F.data == "p_return")
async def pr_first(callback: CallbackQuery, state: FSMContext):
    await state.set_state(PurchaseReturn.reason)
    await callback.message.edit_text("Пожалуйста укажите причину возврат:", reply_markup=kb.reason_kb)


@router2.callback_query(PurchaseReturn.reason)
async def pr_first(callback: CallbackQuery, state: FSMContext):
    await state.update_data(reason=callback)
    await state.set_state(PurchaseReturn.point)
    await callback.message.edit_text("Пожалуйста укажите пункт выдачи", reply_markup=kb.point_kb)


@router2.callback_query(PurchaseReturn.point)
async def pr_third(callback: CallbackQuery, state: FSMContext):
    await state.update_data(reason=callback)
    data = await state.get_data()
    await callback.message.answer(text=f"Ваша заявка успешно принята")
    await state.clear()
