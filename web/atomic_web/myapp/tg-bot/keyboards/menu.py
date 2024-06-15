from aiogram import Bot
from aiogram.types import BotCommand

async def default_commands(bot: Bot):
    menu_commands = [
        BotCommand(command="/start", description="Start bot"),
        BotCommand(command="/help", description="Manual"),
        BotCommand(command="/clear", description="Manual")
    ]

    await bot.set_my_commands(menu_commands)