import asyncio

from aiogram import Bot, Dispatcher, types

from common.config import TOKEN, ALLOWED_UPDATES, private
from handlers.admin_private import admin_router
from handlers.auth_private import auth_router
from handlers.user_private import user_router

cl_bot = Bot(token=TOKEN)

dp = Dispatcher()

dp.include_router(auth_router)
dp.include_router(user_router)
dp.include_router(admin_router)


async def main():
    await cl_bot.delete_webhook(drop_pending_updates=True)
    await cl_bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(cl_bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
