from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Account class.....")

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):

    def __init__(self):
        self.amount = 1000

    def deposit(self, amount):
        self.amount += amount
        print(f"The balance in the account is {self.amount}")

    def getBalance(self):
        print(f"The balance in the account id {self.amount}")


savings = Savings()
savings.deposit(10000)
savings.getBalance()
