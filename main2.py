class BankAccount:

    def __init__(self, owner, balance):  # Исправлено __init__
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Пополнение счета"""
        if amount > 0:
            self.balance += amount
            return f"Баланс пополнен на {amount}. Новый баланс: {self.balance}"
        return "Сумма должна быть больше 0"

    def withdraw(self, amount):
        """Снятие денег"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Вы сняли {amount}, остаток {self.balance}"
        return "Недостаточно средств"

    def get_balance(self):
        """Получение текущего баланса"""
        return f"Текущий баланс: {self.balance}"

# Пример использования
account = BankAccount("Павел Дуров", 10000)
print(account.deposit(5000))
print(account.withdraw(2500))
print(account.get_balance())
