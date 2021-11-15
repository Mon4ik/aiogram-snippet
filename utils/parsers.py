from aiogram.types import *


def keyboard_inline(buttons_list: list[list[InlineKeyboardButton]]) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for row in buttons_list:
        keyboard.row(*row)

    return keyboard


def keyboard_reply(buttons_list: list[list[KeyboardButton]]) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup()

    for row in buttons_list:
        keyboard.row(*row)

    return keyboard
