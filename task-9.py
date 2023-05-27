# Создать класс Rectangle, представляющий прямоугольник по длине и ширине, и метод для вычисления его площади

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

a = float(input('Введите длину прямоугольника: '))
b = float(input('Введите ширину прямоугольника: '))

rectangle = Rectangle(a, b)

print("площадь прямоугольника", rectangle.square())