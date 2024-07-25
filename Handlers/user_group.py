from string import punctuation

from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f

from Filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))  # Кастомный фильтр для роутера


restricted_words = {'кабан', 'нворд'}


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def clean_cmd(message: types.Message):
    # Проверка на вхождение зарпещенного слова в сообщение пользователя группы
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"{message.from_user.full_name}, соблюдайте порядок в чате")
        await message.delete()
        # await message.chat.ban(message.from_user.id)
