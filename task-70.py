# Создайте базу данных для хранения информации о сотрудниках, включающую их имена,
# должности и зарплаты. Затем выведите все имена сотрудников, занимающих должность менеджера.

import sqlite3 as sql

# подключение к базе данных
conn = sql.connect('database.db')
cursor = conn.cursor()    # объект, который создает запросы и получает их результаты

try:
    cursor.execute('''DROP TABLE employes''')   # дроп таблицы
except:
    print("Таблицы employes не существует")


try:
    # создание таблицы
    cursor.execute('''CREATE TABLE employes
                   (id INTEGER PRIMARY KEY, name TEXT, post TEXT, salary INTEGER)''')
except:
    print("Таблица employes создана")


try:
    # Вставка данных в таблицу
    cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Vasya', 'CEO', 1000))
    cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Nadya', 'Менеджер', 2000))
    cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Tolya', 'Сисадмин', 3000))
    cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Viktor', 'Девопс', 4000))

    cursor.execute("SELECT * FROM employes WHERE post is 'Девопс'")  # выборка из таблицы
    rows = cursor.fetchall()   # получение записей из выборки

    for row in rows:
        print(row)      # вывод на экран каждой строки
except:
    # Откат изменений в случае ошибки
    conn.rollback()


conn.close()   # закрытие подключения