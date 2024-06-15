import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from private import TOKEN
from keyboards.menu import default_commands
from handlers import right_hand
from aiogram import F
from aiogram.types import Message

from io import BytesIO

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)

dp = Dispatcher()
dp.include_router(right_hand.router)

dp.startup.register(default_commands)
dp.run_polling(bot)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())