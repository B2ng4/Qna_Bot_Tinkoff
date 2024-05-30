from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from kb import keyboard, keyboard2
from aiogram import Dispatcher, Bot


router = Router()
dp = Dispatcher()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогатор Тинькофф", reply_markup=keyboard)


@router.callback_query()
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == "next":
         await callback_query.message.edit_reply_markup(reply_markup=keyboard2)
    if callback_query.data == "back":
         await callback_query.message.edit_reply_markup(reply_markup=keyboard)

