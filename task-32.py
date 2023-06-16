
# Создайте класс "Школьник". У этого класса должны быть атрибуты "имя" и "класс".
# Создайте метод "учиться", который выводит сообщение, что школьник учится. Создайте
# объект этого класса и вызовите у него метод "учиться".


class Schoolboy:
    def __init__(self, name, classroom):
        self.name = name
        self.classroom = classroom

    def study(self):
        print(f"Школьник учится в {self.classroom} классе")


schoolboy = Schoolboy('Тарантино', 11)
schoolboy.study()