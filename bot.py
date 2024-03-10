import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime
import text
from config_reader import config
from aiogram import F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.formatting import (Bold, as_list, as_marked_section, as_key_value, HashTag)
from aiogram.utils.markdown import hide_link
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

@dp.message(F.text.lower() == "am i alone")
async def cmd_am_i_alone(message: Message):
    await message.answer(
        f"{hide_link('https://demotivatorium.ru/sstorage/3/2023/08/01101645749744/demotivatorium_ru_kak_ponjat_chto_vi_odinoki_220184.jpg')}"
        f"Насколько вы реально одиноки?"
    )


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


@dp.message(F.text.lower() == "content plan")
async def cmd_content_plan(message: types.Message):
    for i in range(len(text.data['name'])):
        if str(text.data['name'][i]) != 'nan':
            await message.answer(f"Дата поста: {str(text.data['date'][i])}\n"
            f"Название поста: {str(text.data['name'][i])}\n"
            f"Автор текста: {str(text.data['text'][i])}\n"
            f"Автор дизайна: {str(text.data['picture'][i])}"
    )


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="bosses"))
    builder.add(types.KeyboardButton(text="bot founder"))
    builder.add(types.KeyboardButton(text="in development"))
    builder.add(types.KeyboardButton(text="hello"))
    builder.add(types.KeyboardButton(text="info"))
    builder.add(types.KeyboardButton(text="am i alone"))
    builder.add(types.KeyboardButton(text="content plan"))
    builder.adjust(2)
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



@dp.message(F.text.lower() == "bot founder")
async def cmd_hidden_link(message: Message):
    await message.answer(
        f"{hide_link('https://vk.com/worldpeacekeaper')}"
        f"<b>Бот лагает</b>\n"
        f"Пользователи: *сука, что за уёбок написал бота*\n"
        f"Уёбок:"
    )


@dp.message(F.text.lower() == "in development")
async def cmd_in_development(message: types.Message):
    await message.answer("В планах добавить в бота должностные лица, расписание постановок, расписание смм, расписание треннингов")


@dp.message(F.text.lower() == "bosses")
async def cmd_bosses(message: types.Message):
    await message.answer(
        "О ком вы бы хотели узнать больше?", reply_markup=get_keyboard()
    )


@dp.callback_query(F.data == "director")
async def send_director(callback: types.callback_query):
    await callback.message.answer("Анастасия Переверзева")


@dp.callback_query(F.data == "organizers")
async def send_organizers(callback: types.callback_query):
    await callback.message.answer("Олеся Крыжановская")


@dp.callback_query(F.data == "dezigners")
async def send_dezigners(callback: types.callback_query):
    await callback.message.answer(
        f"{hide_link('https://www.meme-arsenal.com/memes/f9043fd1f846222cc64e8a929ecaeed5.jpg')}"
        f"Алина Шушкова"
    )


@dp.callback_query(F.data == "smm")
async def send_smm(callback: types.callback_query):
    await callback.message.answer(
        f"{hide_link('https://sun9-7.userapi.com/impg/7aKlRz9lGOzjhRuPSEo2ppcPVFnExSoQMwPQrw/o7wVRmuTIK4.jpg?size=2560x1920&quality=95&sign=9f96785fe91b3b60bb0b67d01096a657&type=album')}"
        f"Дарья Гостева"
    )


@dp.callback_query(F.data == "actors")
async def send_actors(callback: types.callback_query):
    await callback.message.answer(
        f"{hide_link('https://www.meme-arsenal.com/memes/e4cbb27094a83dc2acd2e9fb68194888.jpg')}"
        f"Ася Панина"
    )


@dp.callback_query(F.data == "comand_founder")
async def send_comand_founder(callback: types.callback_query):
    await callback.message.answer(
        f"{hide_link('https://www.meme-arsenal.com/memes/a55ad4ef8fc0f03e7c0feedb538fb736.jpg')}"
        f"Иван Зазулин"
    )


@dp.message(F.text.lower() == "hello")
async def cmd_hello(message: Message):
    await message.answer(
        f"Hello, <u>{message.from_user.full_name}</u>",
        parse_mode=ParseMode.HTML
    )
    

@dp.message(F.text.lower() == "info")
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен: {started_at}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())