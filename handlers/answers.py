from aiogram import Router, F, types, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hide_link

from random import choice
from keyboards.keyboards import get_org_keyboard, get_cp_kb, get_name_cp_kb, get_trenning_kb
from database_prospekt import return_directors, return_content_plan, return_trennings_plan, db, cur
import time
import threading


router = Router()
dp = Dispatcher()
dir = return_directors()
content = return_content_plan()
trennings = return_trennings_plan()


@dp.message_handler(commands=['dz'])
async def process_start_command(message: types.Message):
    dz = CACHE['dz']
    await message.reply(dz)

@router.message(F.text.lower() == "bot founder")
async def cmd_hidden_link(message: Message):
    await message.answer(
        f"{hide_link('https://vk.com/worldpeacekeaper')}"
        f"<b>Бот лагает</b>\n"
        f"Пользователи: кто написал бота*\n"
        f"Я"
    )


@router.message(F.text.lower() == "in development")
async def cmd_in_development(message: types.Message):
    await message.answer("В планах добавить в бота должностные лица, расписание постановок, расписание смм, расписание треннингов")


@router.message(F.text.lower() == "bosses")
async def cmd_bosses(message: types.Message):
    await message.answer(
        "О ком вы бы хотели узнать больше?", reply_markup=get_org_keyboard()
    )


@router.message(F.text.lower() == "am i alone")
async def cmd_am_i_alone(message: Message):
    await message.answer(
        f"{hide_link('https://demotivatorium.ru/sstorage/3/2023/08/01101645749744/demotivatorium_ru_kak_ponjat_chto_vi_odinoki_220184.jpg')}"
        f"Насколько вы реально одиноки?"
    )


@router.message(F.text.lower() == "content plan")
async def cmd_content_plan(message: types.Message):
    await message.answer(
        "Даты на март",
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
