from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard_bt = InlineKeyboardButton(text='1', callback_data='1')
keyboard_bt_next = InlineKeyboardButton(text='-->', callback_data='2')
keyboard_bt_2 = InlineKeyboardButton(text='2', callback_data='3')
keyboard_bt_back = InlineKeyboardButton(text='<--', callback_data='4')

markup = [
    [keyboard_bt],
    [keyboard_bt_next],

]

markup2 = [

    [keyboard_bt_2],
    [keyboard_bt_back]
]

keyboard = InlineKeyboardMarkup(inline_keyboard=markup)
keyboard2 = InlineKeyboardMarkup(inline_keyboard=markup2)