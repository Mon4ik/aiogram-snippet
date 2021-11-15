from dispatcher import dp
from aiogram.types import *
from utils import *

database = db.DBParser("database.sqlite3")


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    """
    On /start

    :param message: User's message
    """

    await message.reply("Welcome to aiogram snippet bot!\nOriginal: https://github.com/Mon4ik/aiogram-snippet")
