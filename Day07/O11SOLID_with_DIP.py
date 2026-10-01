
from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class PayPalGateway(PaymentGateway):

    def pay(self, amount):
        print(f"Paid {amount} using Paypal....")

class StripeGateway(PaymentGateway):

    def pay(self, amount):
        print(f"Paid {amount} using Stripe......")

class PaymentService:

    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def make_payment(self, amount):
        self.gateway.pay(amount)

service1 = PaymentService(PayPalGateway())
service1.make_payment(5000)

service2 = PaymentService(StripeGateway())
service2.make_payment(10000)
