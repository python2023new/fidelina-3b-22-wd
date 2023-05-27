# Создайте класс автомобиль, который имеет свойства "марка", "модель", "год выпуска", "цена".
# Создайте метод вывода информации в формате: " марка - модель, год выпуска, цена"

class Car:

    def __init__(self, brand, model, year_issue, price):
        self.brand = brand
        self.model = model
        self.year_issue = year_issue
        self.price = price

    def car_info(self):
        print(f"{self.brand} - {self.model}, {self.year_issue}, {self.price}")


my_car = Car("Лада", "Калина", "1992", "100000")
my_car.car_info()