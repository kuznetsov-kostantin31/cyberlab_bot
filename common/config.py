from aiogram.fsm.state import StatesGroup, State
from aiogram.types import BotCommand

ADMIN = {
    'max': 'pod_kolecami',
    'kos': 'TINGY31',
    'son': 'tiviomi',
    'art': 'lisoov'
}

TOKEN = '6630291054:AAFNXFOo6poacoD9r35wWslwcus6zlLBaZY'

ALLOWED_UPDATES = ['message', 'edited_message']

private = [
    BotCommand(command='start', description='Начать'),
    BotCommand(command='profile', description='Профиль'),
    BotCommand(command='signup', description='Записаться'),
]


class UserState(StatesGroup):
    data_processing = State()
    collecting_name = State()
