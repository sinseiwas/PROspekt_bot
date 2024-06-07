import unittest
import sqlite3 as sq
from os import path
import os
from answers import *
import mock
from unittest.mock import AsyncMock
from answers import cmd_edit_trennings
from unittest.mock import AsyncMock
import asyncio
from answers import cmd_edit_trennings
 

# Импортируем тестируемые функции
from database_prospekt import (
    edit_trennings, edit_performance, insert_performance, edit_cp, edit_director,
    return_directors, return_content_plan, return_trennings_plan, return_performances, get_script_dir
)

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


    async def test_edit_trennings(self):
            message = AsyncMock()
            await cmd_edit_trennings(message)

            message.answer.assert_called_with('Успешно изменено')

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

if __name__ == '__main__':
    unittest.main()
