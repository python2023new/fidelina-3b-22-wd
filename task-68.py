#Создайте базу данных для хранения информации о книгах, включающую их названия,
# авторов и годы выпуска. Затем выведите все книги, выпущенные после 2000 года.

import sqlite3 as sql

# подключение к базе данных
conn = sql.connect('database.db')

cursor = conn.cursor()  # объект, который создает запросы и получает их результаты

try:
    # дроп таблицы
    cursor.execute('''DROP TABLE books''')
except:
    print("Таблицы books не существует")

try:
    # создание таблицы
    cursor.execute('''CREATE TABLE books
                  (id INTEGER PRIMARY KEY, name TEXT, author TEXT, realise DATE)''')
except:
    print("Таблица books не создана")

try:
    # вставка данных в таблицу
    cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Гарри Поттер', 'Дж.Роулинг', '2003-09-07'))
    cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Закон трех отрицаний', 'Александра Маринина', '2003-11-07'))
    cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Персональный ангел', 'Татьяна Устинова', '1999-01-01'))
    cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Там, где нас нет', 'Татьяна Устинова', '1998-01-01'))

    cursor.execute("SELECT * FROM books WHERE realise >= '2000-01-01'")  # выборка из таблицы

    rows = cursor.fetchall()   # получение записей из выборки
    for row in rows:
        print(row)      # вывод на экран каждой строки
except:
    # Откат изменений в случае ошибки
    conn.rollback()


conn.close()   # закрытие подключения