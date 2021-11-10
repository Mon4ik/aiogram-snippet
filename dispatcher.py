from aiogram import Bot, Dispatcher
import config


bot = Bot(token=config.TOKEN, parse_mode=config.PARSE_MODE)
dp = Dispatcher(bot)
