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


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

@dp.message(Command("am_i_alone"))
async def cmd_am_i_alone(message: Message):
    await message.answer(
        f"{hide_link('https://demotivatorium.ru/sstorage/3/2023/08/01101645749744/demotivatorium_ru_kak_ponjat_chto_vi_odinoki_220184.jpg')}"
        f"Насколько вы реально одиноки?"
    )


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="bosses"))
    builder.add(types.KeyboardButton(text="bot_founder"))
    builder.add(types.KeyboardButton(text="in_development"))
    builder.add(types.KeyboardButton(text="hello"))
    builder.add(types.KeyboardButton(text="info"))
    builder.adjust(2)
    await message.answer(
        f"Привет! Театр ПРОспект приветствует тебя\n",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


@dp.message(F.text.lower() == "bot_founder")
async def cmd_hidden_link(message: Message):
    await message.answer(
        f"{hide_link('https://vk.com/worldpeacekeaper')}"
        f"<b>Бот лагает</b>\n"
        f"Пользователи: *сука, что за уёбок написал бота*\n"
        f"Уёбок:"
    )


@dp.message(F.text.lower() == "in_development")
async def cmd_in_development(message: types.Message):
    await message.answer("В планах добавить в бота должностные лица, расписание постановок, расписание смм, расписание треннингов")


@dp.message(F.text.lower() == "bosses")
async def cmd_bosses(message: types.Message):
    await message.answer(text.prospekt_bosses)


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