import sqlite3 as sq
from os import path

def get_script_dir():
    abs_path = path.abspath(__file__) # полный путь к файлу скрипта
    return path.dirname(abs_path)

DB_NAME = 'prospekt.db'
DB_FILE = get_script_dir() + path.sep + DB_NAME

db = sq.connect(DB_FILE)
# created cursor
cur = db.cursor()

# cur.execute("""CREATE TABLE directors (
#     id integer,
#     name text,
#     post text
# )
# """)

# cur.execute("INSERT INTO directors VALUES('1', 'Ярослав Корнеенко', 'Руководитель')")
# cur.execute("INSERT INTO directors VALUES('2', 'Дарья Гостева', 'Заместитель руководителя')")
# cur.execute("INSERT INTO directors VALUES('3', 'Алиса Паландер', 'Заместитель руководителя')")
# cur.execute("INSERT INTO directors VALUES('4', 'Данил Суханов', 'Куратор СММ, медиа и дизайна')")
# cur.execute("INSERT INTO directors VALUES('5', 'Иван Зазулин', 'Куратор командообразования')")
# cur.execute("INSERT INTO directors VALUES('6', 'Ася Панина', 'Куратор актёров')")
# cur.execute("INSERT INTO directors VALUES('7', 'Пока что нет', 'Куратор организаторов')")


# cur.execute("""CREATE TABLE content_plan (
#     date text,
#     name text,
#     text text,
#     picture text
# )
# """)

# cur.execute("INSERT INTO content_plan VALUES('1.05.2024', 'Мир труд май', 'Даня', 'Ярик')")
# cur.execute("INSERT INTO content_plan VALUES('2.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('3.05.2024', 'Девочки постановка', 'Ярик', 'Дима')")
# cur.execute("INSERT INTO content_plan VALUES('4.05.2024', 'Cheese photo', 'Ярик', 'Ярик')")
# cur.execute("INSERT INTO content_plan VALUES('5.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('6.05.2024', 'Обои от проспекта', 'Даня', 'Алёна')")
# cur.execute("INSERT INTO content_plan VALUES('7.05.2024', 'Завтра премьера', 'Даня', 'Даня')")
# cur.execute("INSERT INTO content_plan VALUES('8.05.2024', 'Сегодня премьера', 'Даня', 'Даня')")
# cur.execute("INSERT INTO content_plan VALUES('9.05.2024', 'С днём победы', 'Даша', 'Ярик')")
# cur.execute("INSERT INTO content_plan VALUES('10.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('11.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('12.05.2024', 'Театральные деятели', 'Диана', 'Диана')")
# cur.execute("INSERT INTO content_plan VALUES('13.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('14.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('15.05.2024', 'Любимая постановка за год', 'Алина', 'Алина')")
# cur.execute("INSERT INTO content_plan VALUES('16.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('17.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('18.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('19.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('20.05.2024', 'История день рождения Ярика', 'Даня', 'Алина')")
# cur.execute("INSERT INTO content_plan VALUES('21.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('22.05.2024', 'Golden voices', 'Сами прислали', 'Сами прислали')")
# cur.execute("INSERT INTO content_plan VALUES('23.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('24.05.2024', 'Итоги года', 'Даня, Ярик', 'Ярик')")
# cur.execute("INSERT INTO content_plan VALUES('25.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('26.05.2024', 'Клип про экзамены', 'Даня', 'Аня')")
# cur.execute("INSERT INTO content_plan VALUES('27.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('28.05.2024', 'Скоро последний зачёт', 'Даша', 'Ярик')")
# cur.execute("INSERT INTO content_plan VALUES('29.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('30.05.2024', '-', '-', '-')")
# cur.execute("INSERT INTO content_plan VALUES('31.05.2024', 'Завтра последний зачёт', 'Даня', 'Даня')")

# cur.execute("""CREATE TABLE trennings (
#     date text,
#     name text,
#     place text
# )
# """)


# cur.execute("INSERT INTO trennings VALUES('1.05.2024', 'Вербатим', '258')")
# cur.execute("INSERT INTO trennings VALUES('2.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('3.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('4.05.2024', 'Вербатим', '-')")
# cur.execute("INSERT INTO trennings VALUES('5.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('6.05.2024', 'Дикция', '367')")
# cur.execute("INSERT INTO trennings VALUES('7.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('8.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('9.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('10.05.2024', 'Вербатим', 'Иннопарк')")
# cur.execute("INSERT INTO trennings VALUES('11.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('12.05.2024', 'Вокал', 'АЗ ГК')")
# cur.execute("INSERT INTO trennings VALUES('13.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('14.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('15.05.2024', 'Дикция', '367')")
# cur.execute("INSERT INTO trennings VALUES('16.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('17.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('18.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('19.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('20.05.2024', 'Дикция', 'АЗ ГК')")
# cur.execute("INSERT INTO trennings VALUES('21.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('22.05.2024', 'Вербатим', '258')")
# cur.execute("INSERT INTO trennings VALUES('23.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('24.05.2024', 'Вербатим', '258')")
# cur.execute("INSERT INTO trennings VALUES('25.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('26.05.2024', 'Вокал', '-')")
# cur.execute("INSERT INTO trennings VALUES('27.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('28.05.2024', 'Вокал', '-')")
# cur.execute("INSERT INTO trennings VALUES('29.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('30.05.2024', '-', '-')")
# cur.execute("INSERT INTO trennings VALUES('31.05.2024', 'Всё вместе', 'АЗ ГК')")

# cur.execute("UPDATE trennings SET place = '-' WHERE date = '31.05.2024'")


def edit_trennings(changed_value_place, changed_value_name, date):
    db = sq.connect(DB_FILE)
    # created cursor
    cur = db.cursor()
    cur.execute(f'UPDATE trennings SET place = "{changed_value_place}" WHERE date = "{date}"')
    cur.execute(f'UPDATE trennings SET name = "{changed_value_name}" WHERE date = "{date}"')
    db.commit()
    db.close()


# def edit_performace(changed_value, date):
#    cur.execute(f'UPDATE trennings SET place = "{changed_value}" WHERE date = "{date}"')


def edit_cp(changed_value_name, changed_value_text, changed_value_picture , date):
    db = sq.connect(DB_FILE)
    # created cursor
    cur = db.cursor()
    cur.execute(f'UPDATE content_plan SET name = "{changed_value_name}" WHERE date = "{date}"')
    cur.execute(f'UPDATE content_plan SET text = "{changed_value_text}" WHERE date = "{date}"')
    cur.execute(f'UPDATE content_plan SET picture = "{changed_value_picture}" WHERE date = "{date}"')
    db.commit()
    db.close()


def edit_director(changed_value, id):
    db = sq.connect(DB_FILE)
    # created cursor
    cur = db.cursor()
    cur.execute(f'UPDATE directors SET name = "{changed_value}" WHERE id = "{id}"')
    db.commit()
    db.close()

def return_directors():
    cur.execute("SELECT * FROM directors")
    return cur.fetchall()
    db.close()

def return_content_plan():
    cur.execute("SELECT * FROM content_plan")
    return cur.fetchall()
    db.close()

def return_trennings_plan():
    cur.execute("SELECT * FROM trennings")
    return cur.fetchall()
    db.close()

def change_table(table_name):
    pass

db.commit()
