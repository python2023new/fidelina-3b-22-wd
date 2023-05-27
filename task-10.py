# Создайте класс Person, описывающий человека со свойствами "имя" и "возраст" и методом для печати этой информации

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_me(self):
        print("Всем приветы! Я - {}, и я стар на {}".format(self.name, self.age))

my_name = str(input('Введите имя: '))
my_age = str(input('Введите возраст: '))

person = Person(my_name, my_age)
person.about_me()