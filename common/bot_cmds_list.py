from aiogram.types import BotCommand

# команды в меню в чате
private = [
    BotCommand(command='start', description='Запустить бота'),
    BotCommand(command='menu', description='Меню'),
    BotCommand(command='about', description='О нас'),
    BotCommand(command='payment', description='Способы оплаты'),
    BotCommand(command='shipping', description='Способы доставки'),
    BotCommand(command='get_id', description='Узнать свой id'),
    BotCommand(command='info', description='Отправить информацию'),
]
