
class PaymentProcessor:

    def process(self, payment_type, amount):
        if payment_type == 'creditcard':
            print(f"Processing {amount} via creditcard")
        elif payment_type == 'paypal':
            print(f"Processing {amount} via paypal")


