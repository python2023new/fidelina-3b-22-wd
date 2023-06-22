# Создать класс "Карточка товара". Реализовать атрибуты "название", "стоимость",
# "количество" и методы "уменьшение количества" и "изменение стоимости" с защитой от
# отрицательного количества и отрицательной стоимости товара.

class ProductCard:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    def decrease_quantity(self, amount):
        self._quantity -= amount
        if self._quantity < 0:
            self._quantity = 0
            print('The quantity cannot be negative!')

    def change_price(self, new_price):
        if new_price < 0:
            print('Price cannot be negative!')
        else:
            self._price = new_price
