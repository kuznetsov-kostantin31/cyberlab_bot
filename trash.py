from aiogram import F, types, Router
from aiogram.filters import CommandStart

auth_router = Router()

@auth_router.message()
async def FIO(message: types.Message):
    user_df[['us_tg']] = message.from_user.username
    user_df[['fio_name']] = message.text
    await message.answer('GROUP')


@auth_router.message()
async def GROUP(message: types.Message):
    user_df[['group']] = message.text
    await message.answer('SUCCESSFUL')


def save_data():
    user_df.to_excel('./cl_db.xlsx', index=False)