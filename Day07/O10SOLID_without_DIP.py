
class PayPalGateway:
    def pay(self, amount):
        print(f"Paid {amount} using paypal")

class PaymentService:

    def __init__(self):
        self.gateway = PayPalGateway()

    def make_payment(self, amount):
        self.gateway.pay(amount)

# client code
service = PaymentService()
service.make_payment(1000)
