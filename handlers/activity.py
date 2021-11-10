from dispatcher import dp
from aiogram.types import *


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    """
    On /start

    :param message: User's message
    """

    await message.reply("Welcome to aiogram snippet bot!\nOriginal: https://github.com/Mon4ik/aiogram-snippet")
