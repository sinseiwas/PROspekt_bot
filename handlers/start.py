from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode

from keyboards.keyboards import get_start_kb


router = Router()
ADMIN_ID = 890684152

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = get_start_kb()
    await message.answer(
        f" Театр ПРОспект приветствует тебя, <u>{message.from_user.full_name}</u>!\n",
        reply_markup=builder.as_markup(resize_keyboard=True),
        parse_mode=ParseMode.HTML
    )
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="ПРОспект", url="https://vk.com/teatr_prospekt")
    )
    await message.answer(
        'Официальная группа вконтакте',
        reply_markup=builder.as_markup(),
    )
    if message.from_user.id == ADMIN_ID:
        await message.answer('1')
