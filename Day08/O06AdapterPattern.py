class OldPaymentSystem:

    def make_payment(self, amount):
        print(f"Payment of {amount} made \nUsing old payment system.....")


class PaymentAdapter:

    def __init__(self, old_payment_system):
        self.old_payment_system = old_payment_system

    def pay(self, amount):
        self.old_payment_system.make_payment(amount)

old_system = OldPaymentSystem()

payment = PaymentAdapter(old_system)

payment.pay(1000)
