class Bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough money!")
        self.balance -= amount

    def print_balance(self):
        print(f"{self.name} {self.balance}")


peter = Bank_account("Peter", 100)
peter.deposit(100)
peter.withdraw(50)
peter.print_balance()