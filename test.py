import unittest
import sqlite3 as sq
import os
from os import path
import asyncio
from unittest.mock import AsyncMock, patch, MagicMock
from aiogram import types
from aiogram.types import Message, CallbackQuery


# Импортируем тестируемые функции
from database_prospekt import (
    edit_trennings, edit_performance, insert_performance, edit_cp, edit_director,
    return_directors, return_content_plan, return_trennings_plan, return_performances, get_script_dir
)
from answers import *
from start import *


class TestDBOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Установка базы данных перед запуском тестов"""
        cls.db_name = 'test_prospekt.db'
        cls.db_file = get_script_dir() + path.sep + cls.db_name
        cls.db = sq.connect(cls.db_file)
        cls.cur = cls.db.cursor()

        # Создаем таблицы
        cls.cur.execute("""
            CREATE TABLE directors (
                id integer,
                name text,
                post text
            )
        """)

        cls.cur.execute("""
            CREATE TABLE content_plan (
                date text,
                name text,
                text text,
                picture text
            )
        """)

        cls.cur.execute("""
            CREATE TABLE trennings (
                date text,
                name text,
                place text
            )
        """)

        cls.cur.execute("""
            CREATE TABLE performances (
                month text,
                date text,
                name text,
                place text
            )
        """)

        cls.db.commit()

    @classmethod
    def tearDownClass(cls):
        """Удаление тестовой базы данных после выполнения тестов"""
        cls.db.close()
        os.remove(cls.db_file)

    def setUp(self):
        """Очистка таблиц перед каждым тестом"""
        self.cur.execute("DELETE FROM directors")
        self.cur.execute("DELETE FROM content_plan")
        self.cur.execute("DELETE FROM trennings")
        self.cur.execute("DELETE FROM performances")
        self.db.commit()


    # async def test_edit_trennings(self):
    #         message = AsyncMock()
    #         await cmd_edit_trennings(message)

    #         message.answer.assert_called_with('Успешно изменено')

    def test_edit_trennings(self):
        self.cur.execute("INSERT INTO trennings VALUES('1.05.2024', 'Вербатим', '258')")
        self.db.commit()
        
        edit_trennings('Новый зал', 'Новая тренировка', '1.05.2024', self.db_file)
        self.cur.execute("SELECT * FROM trennings WHERE date = '1.05.2024'")
        result = self.cur.fetchone()
        
        self.assertEqual(result, ('1.05.2024', 'Новая тренировка', 'Новый зал'))

    def test_edit_performance(self):
        self.cur.execute("INSERT INTO performances VALUES('июнь', '29', 'Слова паразиты', 'Набережная')")
        self.db.commit()
        
        edit_performance('июль', '30', 'Новая постановка', 'Новый зал', '29', 'июнь', self.db_file)
        self.cur.execute("SELECT * FROM performances WHERE date = '30' AND month = 'июль'")
        result = self.cur.fetchone()
        
        self.assertEqual(result, ('июль', '30', 'Новая постановка', 'Новый зал'))

    def test_insert_performance(self):
        insert_performance('август', '15', 'Новое представление', 'Главный зал', self.db_file)
        self.cur.execute("SELECT * FROM performances WHERE date = '15' AND month = 'август'")
        result = self.cur.fetchone()
        
        self.assertEqual(result, ('август', '15', 'Новое представление', 'Главный зал'))

    def test_edit_cp(self):
        self.cur.execute("INSERT INTO content_plan VALUES('1.05.2024', 'Старое событие', 'Старый текст', 'Старая картинка')")
        self.db.commit()
        
        edit_cp('Новое событие', 'Новый текст', 'Новая картинка', '1.05.2024', self.db_file)
        self.cur.execute("SELECT * FROM content_plan WHERE date = '1.05.2024'")
        result = self.cur.fetchone()
        
        self.assertEqual(result, ('1.05.2024', 'Новое событие', 'Новый текст', 'Новая картинка'))

    def test_edit_director(self):
        self.cur.execute("INSERT INTO directors VALUES('1', 'Старый директор', 'Руководитель')")
        self.db.commit()
        
        edit_director('Новый директор', '1', self.db_file)
        self.cur.execute("SELECT * FROM directors WHERE id = '1'")
        result = self.cur.fetchone()
        
        self.assertEqual(result, (1, 'Новый директор', 'Руководитель'))

    def test_return_directors(self):
        self.cur.execute("INSERT INTO directors VALUES('1', 'Директор1', 'Руководитель')")
        self.cur.execute("INSERT INTO directors VALUES('2', 'Директор2', 'Заместитель')")
        self.db.commit()
        
        result = return_directors(self.db_file)
        
        self.assertEqual(result, [(1, 'Директор1', 'Руководитель'), (2, 'Директор2', 'Заместитель')])

    def test_return_content_plan(self):
        self.cur.execute("INSERT INTO content_plan VALUES('1.05.2024', 'Событие1', 'Текст1', 'Картинка1')")
        self.cur.execute("INSERT INTO content_plan VALUES('2.05.2024', 'Событие2', 'Текст2', 'Картинка2')")
        self.db.commit()
        
        result = return_content_plan(self.db_file)
        
        self.assertEqual(result, [
            ('1.05.2024', 'Событие1', 'Текст1', 'Картинка1'),
            ('2.05.2024', 'Событие2', 'Текст2', 'Картинка2')
        ])

    def test_return_trennings_plan(self):
        self.cur.execute("INSERT INTO trennings VALUES('1.05.2024', 'Тренировка1', 'Зал1')")
        self.cur.execute("INSERT INTO trennings VALUES('2.05.2024', 'Тренировка2', 'Зал2')")
        self.db.commit()
        
        result = return_trennings_plan(self.db_file)
        
        self.assertEqual(result, [
            ('1.05.2024', 'Тренировка1', 'Зал1'),
            ('2.05.2024', 'Тренировка2', 'Зал2')
        ])

    def test_return_performances(self):
        self.cur.execute("INSERT INTO performances VALUES('июнь', '29', 'Представление1', 'Место1')")
        self.cur.execute("INSERT INTO performances VALUES('июль', '15', 'Представление2', 'Место2')")
        self.db.commit()
        
        result = return_performances(self.db_file)
        
        self.assertEqual(result, [
            ('июнь', '29', 'Представление1', 'Место1'),
            ('июль', '15', 'Представление2', 'Место2')
        ])


class TestMocking(unittest.IsolatedAsyncioTestCase):
    async def test_edit_trennings(self):
        message = AsyncMock()
        message.from_user.id = 890684152
        message.text = '/edit_trennings param1 param2 31.05.2024'

        await cmd_edit_trennings(message)

        message.answer.assert_called_with('Успешно изменено')

    
    async def test_edit_cp(self):
        message = AsyncMock()
        message.from_user.id = 890684152
        message.text = '/edit_cp param1 param2 param3 31.05.2024'

        await cmd_edit_content_plan(message)

        message.answer.assert_called_with('Успешно изменено')


    async def test_edit_director(self):
        message = AsyncMock()
        message.from_user.id = 890684152
        message.text = '/edit_directors param1 1'

        await cmd_edit_director(message)

        message.answer.assert_called_with('Успешно изменено')

    
    async def test_edit_performace(self):
        message = AsyncMock()
        message.from_user.id = 890684152
        message.text = '/edit_performance param1 param2 param3 param4 param5 param6'

        await cmd_edit_performance(message)

        message.answer.assert_called_with('Успешно изменено')


    async def test_insert_performance(self):
        message = AsyncMock()
        message.from_user.id = 890684152
        message.text = '/insert_performance param1 param2 param3 param4'

        await cmd_insert_performance(message)

        message.answer.assert_called_with('Успешно изменено')
    

    async def test_directors(self):
        message = AsyncMock()

        await cmd_bosses(message)

        message.answer.assert_called_with("О ком вы бы хотели узнать больше?", reply_markup=get_org_keyboard())

    
    async def test_content_plan(self):
        message = AsyncMock()

        await cmd_content_plan(message)

        message.answer.assert_called_with("Даты на май", reply_markup=get_cp_kb())


    async def test_trennings(self):
        message = AsyncMock()

        await cmd_trennings(message)

        message.answer.assert_called_with("Даты на май", reply_markup=get_trenning_kb())
    

    async def test_performances(self):
        message = AsyncMock()

        await cmd_performances(message)

        performances = [
            ['param1', 'param2', 'param3', 'param4'],
        ]

        for i in range(len(performances)):
            message.answer.assert_called_with(f'месяц: {performances[i][0]}\nдата: {performances[i][1]}\nназвание: {performances[i][2]}\nместо проведения: {performances[i][3]}')


    async def test_date_of_post(self):
        callback = AsyncMock()
        callback.data = '1 1'

        await cmd_date_of_post(callback)

        content = return_content_plan()
        i = 1

        callback.message.answer.assert_called_with(f"Дата поста: {str(content[i - 1][0])}\n"
                f"Название поста: {str(content[i - 1][1])}\n"
                f"Автор текста: {str(content[i - 1][2])}\n"
                f"Автор дизайна: {str(content[i - 1][3])}",
                )


    async def test_date_of_trenning(self):
        callback = AsyncMock()
        callback.data = '1 2'

        await cmd_date_of_trenning(callback)

        trennings = return_trennings_plan()
        i = 1

        callback.message.answer.assert_called_with(f"Дата треннинга: {str(trennings[i - 1][0])}\n"
                f"Место проведения: {str(trennings[i - 1][1])}\n"
                f"Место проведения: {str(trennings[i - 1][2])}"
                )
    

    async def test_send_director(self):
        callback = AsyncMock()
        callback.data = '1'

        await cmd_send_director(callback)

        dir = return_directors()
        i = 1

        callback.message.answer.assert_called_with(dir[i - 1][1])

    
    async def test_start_is_admin(self):
        message = AsyncMock()
        message.from_user.id = 890684152
        message.from_user.full_name = "Test User"

        await cmd_start(message)

        builder = get_admin_kb()
        message.answer.assert_any_call(f"Для изменения треннингов введите: /edit_trennings [место, где будет проходить треннинг] [что это будет за треннинг] [дата, когда вы хотите провести треннинг]\nконтент плана: /edit_cp [название поста] [имя того, кто пишет текст] [имя того, кто делает картинку] [дата выхода поста]\nпостановок: /edit_performance\n должностных лиц: /edit_directors [имя, на которое будете менять] [id имени, которое будете менять 1	Ярослав Корнеенко 2 Дарья Гостева 3	Алиса Паландер 4 Данил Суханов 5 Иван Зазулин 6 Ася Панина 7 Пока что нет]\nДаты писать в формате ДД.ММ.ГГГГ",
            reply_markup=builder.as_markup(resize_keyboard=True),
            parse_mode=ParseMode.HTML)

        message.answer.assert_any_call(f" Театр ПРОспект приветствует тебя, <u>{message.from_user.full_name}</u>!\n",
        parse_mode=ParseMode.HTML
        )

        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="ПРОспект", url="https://vk.com/teatr_prospekt")
        )

        message.answer.assert_any_call(
            "Официальная группа вконтакте",
            reply_markup=builder.as_markup()
        )



if __name__ == '__main__':
    unittest.main()
