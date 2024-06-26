
from aiogram import Router, types, Bot
from aiogram.filters import Command
from kb import keyboard_help
from text import START_MESSAGE, additional_questions, HELP_MESSAGE
from gigachat_answers import Ganswer
from config import STICKER_START, STICKER_WAIT
from exctract_json import find_most_similar_title
import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()
bot = Bot(token=config.BOT_TOKEN)

@router.message(Command("start"))
async def start_handler(msg: types.Message):
    await bot.send_sticker(msg.chat.id, STICKER_START)
    await msg.answer(START_MESSAGE)


@router.message(Command("additional_questions"))
async def help_handler(msg: types.Message):
    await msg.answer(additional_questions, reply_markup=keyboard_help)


@router.message(Command("help"))
async def help_handler(msg: types.Message):
    await msg.answer(HELP_MESSAGE, reply_markup=keyboard_help)

@router.message()
async def Generate_answer(msg: types.Message):
    await bot.send_sticker(msg.chat.id, STICKER_WAIT)
    text = msg.text
    response = find_most_similar_title(text)
    keyboard_bt_answer = InlineKeyboardButton(text='Тут находится ответ', url=response[1])
    markup = [
            [keyboard_bt_answer],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=markup)
    await msg.answer(f"\n{Ganswer(text)}", reply_markup=keyboard)
    await msg.answer("📌 Ты можешь задать еще вопрос, если что-то непонятно")

