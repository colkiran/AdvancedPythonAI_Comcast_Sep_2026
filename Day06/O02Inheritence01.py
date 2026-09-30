
class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount} New balance {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdraw {amount} New Balance {self.balance}")
        else:
            print("Insufficient Funds......")

# child class Savings Account

class SavingsAccount(BankAccount):

    def __init__(self, owner, balance, interest_rate=0.05):
        super().__init__(owner, balance)
        self.inter_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.inter_rate
        self.balance += interest
        print(f"Interest added: {interest}, New Balance {self.balance}")

class CurrentAccount(BankAccount):

    def __init__(self, owner, balance=0, overdraft_limit=5000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{self.owner} withdraw {amount} New Balance {self.balance}")
        else:
            print("Overdraft limit exceeded.....")


savings = SavingsAccount("Jack", 85000)
savings.deposit(15000)
savings.add_interest()

print("-" * 60)
current = CurrentAccount("Mike", 30000)
current.withdraw(12500)
current.withdraw(23000)


