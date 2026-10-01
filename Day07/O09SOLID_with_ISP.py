
from abc import ABC, abstractmethod

class Printer(ABC):
    def print(self):
        pass

class Scanner(ABC):
    def scan(self):
        pass

class FaxMachine(ABC):
    def fax(self):
        pass

class BasicPrinter(Printer):

    def print(self):
        print("Printing in progress....")

class MultiFunction(Printer, Scanner, FaxMachine):

    def scan(self):
        print("Scanning the doc...")

    def print(self):
        print("Printing the doc...")

    def fax(self):
        print("Faxing the doc.....")
        