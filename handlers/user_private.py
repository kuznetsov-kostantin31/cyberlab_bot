from aiogram import types, Router
from aiogram.filters import Command

user_router = Router()


@user_router.message(Command('profile'))
async def startBot(message: types.Message):
    await message.answer('Ты кто такой сука?')
