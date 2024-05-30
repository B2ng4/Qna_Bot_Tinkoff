from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from text import URL_START, URL_TAXES, URL_PAY, URL_MAP


"""Клавиатура частых вопросов"""
keyboard_bt_help_1 = InlineKeyboardButton(text='Работа в приложении', url=URL_START)
keyboard_bt_help_2 = InlineKeyboardButton(text='Налоги и взносы',  url=URL_TAXES)
keyboard_bt_help_3 = InlineKeyboardButton(text='Подключение оплаты на сайте',  url=URL_PAY)
keyboard_bt_help_4 = InlineKeyboardButton(text='Перевод за границу',  url=URL_MAP)
keyboard_bt_help_5 = InlineKeyboardButton(text="")

markup_help = [
    [keyboard_bt_help_1, keyboard_bt_help_2],
    [keyboard_bt_help_3, keyboard_bt_help_4],
]

keyboard_help = InlineKeyboardMarkup(inline_keyboard=markup_help)
