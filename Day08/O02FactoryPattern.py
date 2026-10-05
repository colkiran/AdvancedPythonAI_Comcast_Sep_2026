class CreditCard:

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPI:

    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class Cash:

    def pay(self, amount):
        print(f"Paid {amount} using Cash")


class PaymentFactory:
    @staticmethod
    def create_payment(payment_type):

        if payment_type == "credit":
            return CreditCard()

        elif payment_type == "upi":
            return UPI()

        elif payment_type == "cash":
            return Cash()

        else:
            raise ValueError("Invalid Payment Type")

payment = PaymentFactory.create_payment("upi")
payment.pay(10000)

payment = PaymentFactory.create_payment("cash")
payment.pay(3200)
