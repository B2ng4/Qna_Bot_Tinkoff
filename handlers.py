
from aiogram import Router, types, Bot
from aiogram.filters import Command
from kb import keyboard_help
from text import START_MESSAGE, HELP_MESSAGE
from gigachat_answers import Ganswer
from config import STICKER_START, STICKER_WAIT
from exctract_json import find_most_similar_title
import config

router = Router()
bot = Bot(token=config.BOT_TOKEN)

@router.message(Command("start"))
async def start_handler(msg: types.Message):
    await bot.send_sticker(msg.chat.id, STICKER_START)
    await msg.answer(START_MESSAGE, reply_markup=keyboard_help)


@router.message(Command("help"))
async def help_handler(msg: types.Message):
    await msg.answer(HELP_MESSAGE, reply_markup=keyboard_help)


@router.message()
async def Generate_answer(msg: types.Message):
    await bot.send_sticker(msg.chat.id, STICKER_WAIT)
    text = msg.text
    response = find_most_similar_title(text)
    await msg.answer("🔖" + response[0])
    await msg.answer("🔗"+ response[1])
    await msg.answer(Ganswer(text))
    await msg.answer("📌 Ты можешь задать еще вопрос", reply_markup=keyboard_help)

