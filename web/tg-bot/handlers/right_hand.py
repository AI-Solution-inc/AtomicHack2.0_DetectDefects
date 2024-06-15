
from aiogram.exceptions import TelegramBadRequest
from aiogram import Bot, types
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from io import BytesIO
import os

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer('Пожалуйста, загрузите картинку со сварочными швами.')


@router.message(Command('help'))
async def start(message: Message):
    await message.answer('Этот бот поможет найти дефекты на картинках со сварочными швами. Пожалуйста, загрузите картинку.')


@router.message(Command("clear"))
async def all_clear(message: Message, bot: Bot):
    try:
        for i in range(message.message_id, 0, -1):
            await bot.delete_message(message.from_user.id, i)
    except TelegramBadRequest as ex:

        if ex.message == "Bad Request: message to delete not found":
            print("Все сообщения удалены")


@router.message()
async def echo_handler(message: Message) -> None:
    try:
        # в памяти не хранится
        photo = message.send_copy(chat_id=message.chat.id)
        await message.answer(photo)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")

