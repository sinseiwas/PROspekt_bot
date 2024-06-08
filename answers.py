from aiogram import Router, F, types, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hide_link
from aiogram.filters import Command

from random import choice
from start import ADMIN_ID, is_admin
from keyboards.keyboards import get_org_keyboard, get_cp_kb, get_name_cp_kb, get_trenning_kb, get_admin_kb, get_admin_trenning_kb
from database_prospekt import return_directors, return_content_plan, return_trennings_plan, return_performances, edit_cp, edit_trennings, edit_director, edit_performance, insert_performance
import time
import threading


router = Router()
dp = Dispatcher()


@router.message(Command("edit_trennings"))
async def cmd_edit_trennings(message: types.Message):
    # if is_admin(message.from_user.id):
    #     global user_message
    #     user_message = message.text.split()
    #     edit_trennings(user_message[1], user_message[2], user_message[3])
        await message.answer(
            'Успешно изменено'
        )


@router.message(Command("edit_cp"))
async def cmd_edit_content_plan(message: types.Message):
    # if is_admin(message.from_user.id):
    #     global user_message
    #     user_message = message.text.split()
    #     edit_cp(user_message[1], user_message[2], user_message[3], user_message[4])
    #     print(user_message)
        await message.answer(
            'Успешно изменено'
        )


@router.message(Command("edit_director"))
async def cmd_edit_director(message: types.Message):
    # if is_admin(message.from_user.id):
    #     global user_message
    #     user_message = message.text.split()
    #     edit_director(user_message[1], user_message[2])
    #     print(user_message)
        await message.answer(
            'Успешно изменено'
        )


@router.message(Command("edit_performance"))
async def cmd_edit_performance(message: types.Message):
    if is_admin(message.from_user.id):
        global user_message
        user_message = message.text.split()
        print(user_message)
        edit_performance(user_message[1], user_message[2], user_message[3], user_message[4], user_message[5], user_message[6])
        await message.answer(
            'Успешно изменено'
        )


@router.message(Command("insert_performance"))
async def cmd_insert_performance(message: types.Message):
    if is_admin(message.from_user.id):
        global user_message
        user_message = message.text.split()
        print(user_message)
        insert_performance(user_message[1], user_message[2], user_message[3], user_message[4])
        print(user_message)
        await message.answer(
            'Успешно изменено'
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


@router.message(F.text.lower() == "trennings")
async def cmd_trennings(message: types.Message):
    await message.answer(
        "Даты на май",
        reply_markup=get_trenning_kb()
    )


@router.message(F.text.lower() == "performances")
async def cmd_performances(message: types.Message):
    performances = return_performances()
    print(performances)
    for i in range(len(performances)):
        await message.answer(
                f'месяц: {performances[i][0]}\nдата: {performances[i][1]}\nназвание: {performances[i][2]}\nместо проведения: {performances[i][3]}'
        )


for i in range(1,len(return_content_plan()) + 1):
    if F.data == f'{str(i)} 1':
        @router.callback_query(F.data == f'{str(i)} 1')
        async def date_of_post(callback: types.CallbackQuery):
            i = int(callback.data[:2])
            content = return_content_plan()
            await callback.message.answer(
                f"Дата поста: {str(content[i - 1][0])}\n"
                f"Название поста: {str(content[i - 1][1])}\n"
                f"Автор текста: {str(content[i - 1][2])}\n"
                f"Автор дизайна: {str(content[i - 1][3])}",
            )
            await callback.answer()


for i in range(1, len(return_trennings_plan()) + 1):
    if F.data == f'{str(i)} 2':
        @router.callback_query(F.data == f'{str(i)} 2')
        async def date_of_trenning(callback: types.CallbackQuery):
            i = int(callback.data[:2])
            trennings = return_trennings_plan()
            await callback.message.answer(
                f"Дата треннинга: {str(trennings[i - 1][0])}\n"
                f"Место проведения: {str(trennings[i - 1][1])}\n"
                f"Место проведения: {str(trennings[i - 1][2])}"

            )
            await callback.answer()


for i in range(1, len(return_directors()) + 1):
    if F.data == str(i):
        @router.callback_query(F.data == str(i))
        async def send_director(callback: types.callback_query):
            i = int(callback.data)
            dir = return_directors()
            await callback.message.answer(dir[i - 1][1])
            await callback.answer()
