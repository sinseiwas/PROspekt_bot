from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types


import exel


def get_org_keyboard():
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


def get_cp_kb():
    buttons = []
    for i in range(1, 32, 4):
        row = [
            types.InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"),
            types.InlineKeyboardButton(text=f"{i + 1}", callback_data=f"{i + 1}"),
            types.InlineKeyboardButton(text=f"{i + 2}", callback_data=f"{i + 2}")
        ]
        if i + 3 != 32:
            row.append(types.InlineKeyboardButton(text=f"{i + 3}", callback_data=f"{i + 3}"))
        buttons.append(row)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_name_cp_kb():
    buttons = []
    for i in text.names:
        types.InlineKeyboardButton(text=f"{i}", callback_data=f"{i}")
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_start_kb():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="bosses"))
    builder.add(types.KeyboardButton(text="bot founder"))
    builder.add(types.KeyboardButton(text="in development"))
    builder.add(types.KeyboardButton(text="am i alone"))
    builder.add(types.KeyboardButton(text="content plan"))
    builder.adjust(2)

    return builder