
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def process(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):

    def process(self, amount):
        print(f"Processing {amount} via Credit Card")

class PayPalPayment(PaymentProcessor):

    def process(self, amount):
        print(f"Processing {amount} via PayPal")

class UpiPayment(PaymentProcessor):

    def process(self, amount):
        print(f"Processing {amount} via UPI")