from aiogram import Router, F, types, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hide_link
from aiogram.filters import Command

from random import choice
from keyboards.keyboards import get_org_keyboard, get_cp_kb, get_name_cp_kb, get_trenning_kb, get_admin_kb, get_admin_trenning_kb
from database_prospekt import return_directors, return_content_plan, return_trennings_plan, edit_cp, edit_trennings, edit_director
import time
import threading


router = Router()
dp = Dispatcher()
dir = return_directors()
content = return_content_plan()
trennings = return_trennings_plan()
ADMIN_ID = 890684152


@router.message(Command("edit_trennings"))
async def cmd_content_plan(message: types.Message):

    global user_message
    user_message = message.text.split()
    edit_trennings(user_message[1], user_message[2], user_message[3])
    print(user_message)
    await message.answer(
        'Успешно изменено'
    )


@router.message(Command("edit_cp"))
async def cmd_content_plan(message: types.Message):
    global user_message
    user_message = message.text.split()
    edit_cp(user_message[1], user_message[2], user_message[3], user_message[4])
    print(user_message)
    await message.answer(
        'Успешно изменено'
    )


@router.message(Command("edit_director"))
async def cmd_content_plan(message: types.Message):
    global user_message
    user_message = message.text.split()
    edit_director(user_message[1], user_message[2])
    print(user_message)
    await message.answer(
        'Успешно изменено'
    )


for i in range(1, 32):
    if F.data == f'{str(i)} 2':
        @router.callback_query(F.data == f'{str(i)} a')
        async def date_of_post(callback: types.CallbackQuery):
            what_2 = 1
            i = int(callback.data[:2])
            await callback.message.answer(
                'На какой треннинг вы хотети поменять на эту дату?'

            )


@router.message(F.text.lower() == "directors")
async def cmd_bosses(message: types.Message):
    await message.answer(
        "О ком вы бы хотели узнать больше?", reply_markup=get_org_keyboard()
    )


@router.message(F.text.lower() == "content plan")
async def cmd_content_plan(message: types.Message):
    await message.answer(
        "Даты на май",
        reply_markup=get_cp_kb()
    )
    await message.answer(
        "Тексты на март",
        reply_markup=get_name_cp_kb
    )


@router.message(F.text.lower() == "trennings")
async def cmd_content_plan(message: types.Message):
    await message.answer(
        "Даты на май",
        reply_markup=get_trenning_kb()
    )


for i in range(1, 32):
    if F.data == f'{str(i)} 1':
        @router.callback_query(F.data == f'{str(i)} 1')
        async def date_of_trenning(callback: types.CallbackQuery):
            i = int(callback.data[:2])
            await callback.message.answer(
                f"Дата поста: {str(content[i - 1][0])}\n"
                f"Название поста: {str(content[i - 1][1])}\n"
                f"Автор текста: {str(content[i - 1][2])}\n"
                f"Автор дизайна: {str(content[i - 1][3])}",
            )

for i in range(1, 32):
    if F.data == f'{str(i)} 2':
        @router.callback_query(F.data == f'{str(i)} 2')
        async def date_of_post(callback: types.CallbackQuery):
            i = int(callback.data[:2])
            print(i)
            await callback.message.answer(
                f"Дата треннинга: {str(trennings[i - 1][0])}\n"
                f"Место проведения: {str(trennings[i - 1][1])}\n"
                f"Место проведения: {str(trennings[i - 1][2])}"

            )

for i in range(1, 8):
    if F.data == str(i):
        @router.callback_query(F.data == str(i))
        async def send_director(callback: types.callback_query):
            i = int(callback.data)
            await callback.message.answer(dir[i - 1][1])
