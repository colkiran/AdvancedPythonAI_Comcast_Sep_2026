
class CreditCard:

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPI:

    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class Cash:

    def pay(self, amount):
        print(f"Paid {amount} using Cash")

payment_type = "Cash"
if payment_type == "UPI":
    upi = UPI()
    upi.pay(3500)
elif payment_type == "Cash":
    cash = Cash()       # using a new operator
    cash.pay(6500)
elif payment_type == "CreditCard":
    cc = CreditCard()
    cc.pay(7000)
    