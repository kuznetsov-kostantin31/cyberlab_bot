from aiogram import types, Router, F
from aiogram.filters import CommandStart
import pandas as pd

auth_router = Router()
user_df = pd.read_excel('./cl_db.xlsx', sheet_name='usernames')


def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Да", callback_data="yes"),
            types.InlineKeyboardButton(text="Нет", callback_data="no")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@auth_router.message(CommandStart())
async def startBot(message: types.Message):
    await message.answer("Перед началом работы бота: согласны ли вы на обработку персональных данных?",
                         reply_markup=get_keyboard())


@auth_router.message()
@auth_router.callback_query(F.data == 'yes')
async def callback_data(callback: types.CallbackQuery, message: types.Message):
    action = callback.data

    if action == "yes":
        await message.answer("Вы являетесь сотрудником/студентом ВВГУ", reply_markup=get_keyboard())
    elif action == "no":
        await message.answer("Тогда хорошего вам дня ✨")
    await callback.answer()



