#Создайте базу данных для хранения информации о фильмах, включающую их названия,
# жанры и рейтинги. Затем выведите все фильмы выбранного жанра.

import sqlite3 as sql

# подключение к базе данных
conn = sql.connect('database.db')
cursor = conn.cursor()    # объект, который создает запросы и получает их результаты

try:
    cursor.execute('''DROP TABLE films''')   # дроп таблицы
except:
    print("Таблицы books не существует")

try:
    # создание таблицы
    cursor.execute('''CREATE TABLE films
                  (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating INTEGER)''')
except:
    print("Таблица films не создана")

try:

    # вставка данных в таблицу
    cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Васаби', 'боевик', 9.7))
    cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Копы в юбках', 'комедия', 8.6))
    cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Девичник в Вегасе', 'романтика', 8.9))
    cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Берегись автомобиля', 'криминал', 7.6))

    cursor.execute("SELECT * FROM films WHERE genre is 'комедия'")  # выборка из таблицы
    rows = cursor.fetchall()   # получение записей из выборки

    for row in rows:
        print(row)      # вывод на экран каждой строки
except:
    # Откат изменений в случае ошибки
    conn.rollback()


conn.close()   # закрытие подключения