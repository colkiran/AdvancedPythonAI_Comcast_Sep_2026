
class Payment:

    def pay(self, amount):
        pass


class OLDPaymentSystem:

    def make_payment(self, amount):
        print(f"payment of {amount} is made using old payment system")

class PaymentAdapter:

    def __init__(self, old_payment_system):
        self.old_payment_system = old_payment_system

    def pay(self, amount):
        self.old_payment_system.make_payment(amount)
