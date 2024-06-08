from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types


def get_org_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Руководитель", callback_data="1"),
            types.InlineKeyboardButton(text="Заместители", callback_data="2")
        ],
        [
            types.InlineKeyboardButton(text="Организатор", callback_data="7"),
            types.InlineKeyboardButton(text="СММ", callback_data="4")
        ],
        [
            types.InlineKeyboardButton(text="Куратор актёров", callback_data="6"),
            types.InlineKeyboardButton(text="Куратор командообразования", callback_data="5")
        ]
    ]


    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_cp_kb():
    buttons = []
    for i in range(1, 32, 4):
        row = [
            types.InlineKeyboardButton(text=f"{i}", callback_data=f"{i} 1"),
            types.InlineKeyboardButton(text=f"{i + 1}", callback_data=f"{i + 1} 1"),
            types.InlineKeyboardButton(text=f"{i + 2}", callback_data=f"{i + 2} 1")
        ]
        if i + 3 != 32:
            row.append(types.InlineKeyboardButton(text=f"{i + 3}", callback_data=f"{i + 3} 1"))
        buttons.append(row)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_trenning_kb():
    buttons = []
    for i in range(1, 32, 4):
        row = [
            types.InlineKeyboardButton(text=f"{i}", callback_data=f"{i} 2"),
            types.InlineKeyboardButton(text=f"{i + 1}", callback_data=f"{i + 1} 2"),
            types.InlineKeyboardButton(text=f"{i + 2}", callback_data=f"{i + 2} 2")
        ]
        if i + 3 != 32:
            row.append(types.InlineKeyboardButton(text=f"{i + 3}", callback_data=f"{i + 3} 2"))
        buttons.append(row)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_admin_trenning_kb():
    buttons = []
    for i in range(1, 32, 4):
        row = [
            types.InlineKeyboardButton(text=f"{i}", callback_data=f"{i} a"),
            types.InlineKeyboardButton(text=f"{i + 1}", callback_data=f"{i + 1} a"),
            types.InlineKeyboardButton(text=f"{i + 2}", callback_data=f"{i + 2} a")
        ]
        if i + 3 != 32:
            row.append(types.InlineKeyboardButton(text=f"{i + 3}", callback_data=f"{i + 3} a"))
        buttons.append(row)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_start_kb():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="directors"))
    builder.add(types.KeyboardButton(text="content plan"))
    builder.add(types.KeyboardButton(text="trennings"))
    builder.add(types.KeyboardButton(text="performances"))
    builder.adjust(2)

    return builder

def get_admin_kb():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="directors"))
    builder.add(types.KeyboardButton(text="content plan"))
    builder.add(types.KeyboardButton(text="trennings"))
    builder.add(types.KeyboardButton(text="performances"))
    builder.adjust(2)

    return builder