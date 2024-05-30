
from aiogram import Router, types, Bot
from aiogram.filters import Command
from kb import keyboard_help
from text import START_MESSAGE, HELP_MESSAGE
from gigachat_answers import Ganswer
from config import STICKER_START, STICKER_WAIT
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
    await msg.answer(Ganswer(text))
    await msg.answer("Ты можешь еще задать вопрос", reply_markup=keyboard_help)

