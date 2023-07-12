#Создайте базу данных для хранения информации о студентах, включающую их имена,
# возраст и средний балл. Затем выведите все данные на экран.

import sqlite3 as sql


# Подключение к БД
conn = sql.connect('database.db')

try:
    # выполнение операций
    #BEGIN TRANSACTION;
    # создание таблицы
    cursor = conn.cursor()  # создает запросы и получает их результаты
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, avarage_score INTEGER)''')

    # вставка данных в таблицу
    cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('John Dep', 21, 4))
    cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('Chris Robinson', 25, 5))
    cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('Bob Chick', 19, 3))
    cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('Sofia Formula', 27, 4))

    cursor.execute("SELECT * FROM students")  # выборка из таблицы
    rows = cursor.fetchall()  # получение записей из выборки

    # создание таблицы
    cursor = conn.cursor()  # объект, который создает запросы и получает их результаты
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, avarage_score INTEGER)''')

    # вставка данных в таблицу
    cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('John Myr', 21, 4))
    cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('Chris Redis', 25, 5))
    cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('Bob Pop', 20, 3))
    cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('Sofia Tod', 29, 4))

    cursor.execute("SELECT * FROM students")  # выборка из таблицы
    rows = cursor.fetchall()  # получение записей из выборки

    for row in rows:
        print(row)  # вывод на экран каждой строки
except:
    # Откат изменений в случае ошибки
    conn.rollback()


# закрытие подключения
conn.close()