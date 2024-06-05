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


# cur.execute("""CREATE TABLE performances (
#     month text,
#     date text,
#     name text,
#     place text
# )
# """)

# cur.execute("INSERT INTO performances VALUES('june', '29', 'Слова паразиты', 'Набережная')")
# cur.execute("INSERT INTO performances VALUES('july', '15', 'Клоун Аристотель', 'АЗ ГК')")
# cur.execute("INSERT INTO performances VALUES('july', '30', 'Времена года', 'АЗ ГК')")
# cur.execute("INSERT INTO performances VALUES('august', '15', '12', 'АЗ ГК')")
# cur.execute("UPDATE performances SET month = 'июнь' WHERE month = 'june'")
# cur.execute("UPDATE performances SET month = 'июль' WHERE month = 'july'")
# cur.execute("UPDATE performances SET month = 'август' WHERE month = 'august'")


def edit_trennings(changed_value_place, changed_value_name, date):
    db = sq.connect(DB_FILE)
    # created cursor
    cur = db.cursor()
    cur.execute(f'UPDATE trennings SET place = "{changed_value_place}" WHERE date = "{date}"')
    cur.execute(f'UPDATE trennings SET name = "{changed_value_name}" WHERE date = "{date}"')
    db.commit()


def edit_performance(changed_value_month, changed_value_date, changed_value_name, changed_value_place, date, month):
    db = sq.connect(DB_FILE)
    # created cursor
    cur = db.cursor()
    cur.execute(f'UPDATE performances SET month = "{changed_value_month}" WHERE date = "{date}" AND month = "{month}"')
    cur.execute(f'UPDATE performances SET date = "{changed_value_date}" WHERE date = "{date}" AND month = "{changed_value_month}"')
    cur.execute(f'UPDATE performances SET name = "{changed_value_name}" WHERE date = "{changed_value_date}" AND month = "{changed_value_month}"')
    cur.execute(f'UPDATE performances SET place = "{changed_value_place}" WHERE date = "{changed_value_date}" AND month = "{changed_value_month}"')
    db.commit()


def insert_performance(month, date, name, place):
    db = sq.connect(DB_FILE)
    # created cursor
    cur = db.cursor()
    cur.execute(f'INSERT INTO performances VALUES("{month}", "{date}", "{name}", "{place}")')
    db.commit()


def edit_cp(changed_value_name, changed_value_text, changed_value_picture , date):
    db = sq.connect(DB_FILE)
    # created cursor
    cur = db.cursor()
    cur.execute(f'UPDATE content_plan SET name = "{changed_value_name}" WHERE date = "{date}"')
    cur.execute(f'UPDATE content_plan SET text = "{changed_value_text}" WHERE date = "{date}"')
    cur.execute(f'UPDATE content_plan SET picture = "{changed_value_picture}" WHERE date = "{date}"')
    db.commit()


def edit_director(changed_value, id):
    cur.execute(f'UPDATE directors SET name = "{changed_value}" WHERE id = "{id}"')
    db.commit()

def return_directors():
    cur.execute("SELECT * FROM directors")
    return cur.fetchall()

def return_content_plan():
    cur.execute("SELECT * FROM content_plan")
    return cur.fetchall()

def return_trennings_plan():
    cur.execute("SELECT * FROM trennings")
    return cur.fetchall()


def return_performances():
    cur.execute("SELECT * FROM performances")
    return cur.fetchall()

def change_table(table_name):
    pass


db.commit()
