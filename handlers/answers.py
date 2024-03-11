from aiogram import Router, F, types, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hide_link


from random import choice
import exel
from keyboards.keyboards import get_org_keyboard, get_cp_kb, get_name_cp_kb



router = Router()
dp = Dispatcher()


@router.message(F.text.lower() == "bot founder")
async def cmd_hidden_link(message: Message):
    await message.answer(
        f"{hide_link('https://vk.com/worldpeacekeaper')}"
        f"<b>Бот лагает</b>\n"
        f"Пользователи: *сука, что за уёбок написал бота*\n"
        f"Уёбок:"
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

for i in range(1, 32):
    if F.data == str(i):
        @router.callback_query(F.data == str(i))
        async def date_of_post(callback: types.CallbackQuery):
            i = int(callback.data)
            await callback.message.answer(
                f"Дата поста: {str(exel.data['date'][i - 1])}\n"
                f"Название поста: {str(exel.data['name'][i - 1])}\n"
                f"Автор текста: {str(exel.data['text'][i - 1])}\n"
                f"Автор дизайна: {str(exel.data['picture'][i - 1])}",
            )



@router.callback_query(F.data == "director")
async def send_director(callback: types.callback_query):
    await callback.message.answer("Анастасия Переверзева")


@router.callback_query(F.data == "organizers")
async def send_organizers(callback: types.callback_query):
    await callback.message.answer("Олеся Крыжановская")


@router.callback_query(F.data == "dezigners")
async def send_dezigners(callback: types.callback_query):
    await callback.message.answer(
        f"{hide_link('https://www.meme-arsenal.com/memes/f9043fd1f846222cc64e8a929ecaeed5.jpg')}"
        f"Алина Шушкова"
    )


@router.callback_query(F.data == "smm")
async def send_smm(callback: types.callback_query):
    await callback.message.answer(
        f"{hide_link('https://sun9-7.userapi.com/impg/7aKlRz9lGOzjhRuPSEo2ppcPVFnExSoQMwPQrw/o7wVRmuTIK4.jpg?size=2560x1920&quality=95&sign=9f96785fe91b3b60bb0b67d01096a657&type=album')}"
        f"Дарья Гостева"
    )


@router.callback_query(F.data == "actors")
async def send_actors(callback: types.callback_query):
    await callback.message.answer(
        f"{hide_link('https://www.meme-arsenal.com/memes/e4cbb27094a83dc2acd2e9fb68194888.jpg')}"
        f"Ася Панина"
    )


@router.callback_query(F.data == "comand_founder")
async def send_comand_founder(callback: types.callback_query):
    await callback.message.answer(
        f"{hide_link('https://www.meme-arsenal.com/memes/a55ad4ef8fc0f03e7c0feedb538fb736.jpg')}"
        f"Иван Зазулин"
    )