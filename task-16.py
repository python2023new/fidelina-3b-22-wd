#  Создайте класс кошка, у которой есть имя, возраст и цвет.
#Создайте метод, который выводит информацию о кошке в формате: " кошка по имени Имя, Возраст лет, цвет Цвет"

class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def cat_info(self):
        print(f"Кошка по имени {self.name}, возраст {self.age}, цвет {self.color}")

my_cat = Cat("Маруся", 5, "золотой")
my_cat.cat_info()