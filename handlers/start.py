from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.keyboards import get_start_kb


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = get_start_kb()
    await message.answer(
        f"Привет! Театр ПРОспект приветствует тебя\n",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="ПРОспект", url="https://vk.com/teatr_prospekt")
    )
    await message.answer(
        'Официальная группа вконтакте',
        reply_markup=builder.as_markup(),
    )
