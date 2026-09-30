
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        print(self.__balance)

myaccount = BankAccount(50000)
myaccount.deposit(35000)
myaccount.get_balance()


