from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types


def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Режисёры", callback_data="director"),
            types.InlineKeyboardButton(text="Организаторы", callback_data="organizers")
        ],
        [
            types.InlineKeyboardButton(text="Дизайнеры", callback_data="dezigners"),
            types.InlineKeyboardButton(text="СММ", callback_data="smm")
        ],
        [
            types.InlineKeyboardButton(text="Куратор актёров", callback_data="actors"),
            types.InlineKeyboardButton(text="Куратор командообразования", callback_data="comand_founder")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_start_kb():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="bosses"))
    builder.add(types.KeyboardButton(text="bot founder"))
    builder.add(types.KeyboardButton(text="in development"))
    builder.add(types.KeyboardButton(text="hello"))
    builder.add(types.KeyboardButton(text="am i alone"))
    builder.add(types.KeyboardButton(text="content plan"))
    builder.adjust(2)

    return builder