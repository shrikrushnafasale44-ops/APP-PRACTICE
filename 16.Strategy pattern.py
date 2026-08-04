class Payment:
    def pay(self):
        print("Making payment")


class UPI(Payment):
    def pay(self):
        print("Payment through UPI")


class Card(Payment):
    def pay(self):
        print("Payment through Card")


def make_payment(method):
    method.pay()


choice = UPI()
make_payment(choice)
