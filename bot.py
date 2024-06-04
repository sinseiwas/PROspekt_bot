import asyncio
from aiogram import Bot, Dispatcher
from handlers import start, answers
from aiogram.utils.markdown import hide_link

from database_prospekt import get_script_dir, DB_NAME, DB_FILE


async def main():
    bot = Bot(token="6974256244:AAFwzF8cqPoSN_jiHPdu1Mw9PDChUCyRQv0", parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(start.router, answers.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())