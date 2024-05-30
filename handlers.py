from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from kb import keyboard_help
from aiogram import Dispatcher, Bot


router = Router()
dp = Dispatcher()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогатор Тинькофф!\nТы можешь выбрать вопрос на который уже есть ответ, а можешь задать прямо сейчас!", reply_markup=keyboard_help)


@router.callback_query()
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == "next":
        return None


