from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from text import URL_START, URL_TAXES

keyboard_bt_help_1 = InlineKeyboardButton(text='Как начать работу в приложении', url=URL_START)
keyboard_bt_next = InlineKeyboardButton(text='-->', callback_data='next')
keyboard_bt_help_2 = InlineKeyboardButton(text='Как платить налоги и взносы',  url=URL_TAXES)
keyboard_bt_back = InlineKeyboardButton(text='<--', callback_data='back')

markup = [
    [keyboard_bt_help_1],
    [keyboard_bt_next],

]

markup2 = [

    [keyboard_bt_help_2],
    [keyboard_bt_back]
]

keyboard = InlineKeyboardMarkup(inline_keyboard=markup)
keyboard2 = InlineKeyboardMarkup(inline_keyboard=markup2)