# Создать класс "Банк", который хранит информацию о клиентах, счетах и транзакциях.
# Реализовать методы для создания клиента и открытия счета, а также для совершения
# перевода с одного счета на другой с проверкой на наличие достаточной суммы на
# счете.

class Bank:
    def __init__(self):
        self.clients = {}

    def add_client(self, name):
        if name not in self.clients:
            self.clients[name] = {}

    def open_account(self, name, account_number, balance):
        if name in self.clients:
            if account_number not in self.clients[name]:
                self.clients[name][account_number] = balance
                print(f"Account {account_number} opened for {name} with initial balance of {balance}")
            else:
                print(f"Account {account_number} already exists for {name}")
        else:
            print(f"No client found with name {name}")

    def transfer(self, from_name, from_account_number, to_name, to_account_number, amount):
        if from_name in self.clients and to_name in self.clients:
            if from_account_number in self.clients[from_name] and to_account_number in self.clients[to_name]:
                if self.clients[from_name][from_account_number] >= amount:
                    self.clients[from_name][from_account_number] -= amount
                    self.clients[to_name][to_account_number] += amount
                    print(f"Transfer of {amount} from account {from_account_number} of {from_name} to account {to_account_number} of {to_name} has been completed")
                else:
                    print(f"Insufficient balance in account {from_account_number} of {from_name} for the amount of {amount}")
            else:
                print(f"No account found for {from_name} or {to_name}")
        else:
            print(f"No client found for {from_name} or {to_name}")


