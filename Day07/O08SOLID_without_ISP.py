
from abc import ABC, abstractmethod

class Machine(ABC):

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def fax(self):
        pass

class BasicPrinter(Machine):

    def print(self):
        print("Printing in process.....")

    def scan(self):
        raise NotImplementedError("BasicPrint cannot scan")

    def fax(self):
        raise NotImplementedError("BasicPrint cannot fax")
