import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)
bot = Bot(token="6974256244:AAFwzF8cqPoSN_jiHPdu1Mw9PDChUCyRQv0")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


async def cmd_test2(message: types.Message):
    await message.reply("Test 2")

@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')


@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


async def main():
    await dp.start_polling(bot)
    dp.message.register(cmd_test2, Command("test2"))


if __name__ == "__main__":
    asyncio.run(main())