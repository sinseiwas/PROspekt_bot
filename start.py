from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode

from keyboards.keyboards import get_start_kb, get_admin_kb


router = Router()
ADMIN_ID = (890684152, 943191156)
def is_admin(user_id):
    for i in range(len(ADMIN_ID)):
        if user_id == ADMIN_ID[i]:
            return 1
    return 0

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    if not is_admin(message.from_user.id):
        builder = get_start_kb()
    else:
        builder = get_admin_kb()
        await message.answer(
            f"Для изменения треннингов введите: /edit_trennings [место, где будет проходить треннинг] [что это будет за треннинг] [дата, когда вы хотите провести треннинг]\nконтент плана: /edit_cp [название поста] [имя того, кто пишет текст] [имя того, кто делает картинку] [дата выхода поста]\nпостановок: /edit_performance\n должностных лиц: /edit_directors [имя, на которое будете менять] [id имени, которое будете менять 1	Ярослав Корнеенко 2 Дарья Гостева 3	Алиса Паландер 4 Данил Суханов 5 Иван Зазулин 6 Ася Панина 7 Пока что нет]\nДаты писать в формате ДД.ММ.ГГГГ",
            reply_markup=builder.as_markup(resize_keyboard=True),
            parse_mode=ParseMode.HTML
        )
    await message.answer(
        f" Театр ПРОспект приветствует тебя, <u>{message.from_user.full_name}</u>!\n",
        parse_mode=ParseMode.HTML
    )
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="ПРОспект", url="https://vk.com/teatr_prospekt")
    )
    await message.answer(
        'Официальная группа вконтакте',
        reply_markup=builder.as_markup(),
    )
