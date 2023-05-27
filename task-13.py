# Создайте класс "BankAccount", описывающий банковский счет со свойствами: "имя вледельца", "номер счета", "баланс"
# и методом для пополнения и снятия средств со счета


class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def add_money(self, money):
        self.balance += money

    def withdraw_money(self, money):
        self.balance -= money


acc = BankAccount("Иван", 4000000002801, 202026782020)

acc.add_money(1)
print(acc.balance)

acc.withdraw_money(2)
print(acc.balance)

