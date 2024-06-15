from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# определим кнопки на всякий случай
class InlineKeyboard:
    @property
    def start(self):

        inline_keyboard = [
            [types.InlineKeyboardButton(text='Some options', callback_data='options'),
             types.InlineKeyboardButton(text="Download", callback_data="download"),]
        ]
        return types.InlineKeyboardMarkup(inline_keyboard=inline_keyboard)