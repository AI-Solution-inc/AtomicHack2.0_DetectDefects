import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from private import TOKEN
from keyboards.menu import default_commands
from handlers import right_hand
from aiogram import F
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)

dp = Dispatcher()
dp.include_router(right_hand.router)

dp.startup.register(default_commands)
dp.run_polling(bot)

async def main():
    await dp.start_polling(bot)


# @dp.message(content_types=['photo'])
# async def get_photos(message: types.Message):
#     file_info = await bot.get_file(message.photo[-1].file_id)
#     await message.photo[-1].download(file_info.file_path.split('photos/')[1])

# @dp.message(F.photo)
# async def get_photo(message: Message):
#     file_id = message.photo[-1]
#     await message.answer_photo(photo=file_id)




if __name__ == '__main__':
    asyncio.run(main())