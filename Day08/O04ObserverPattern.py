
class User:

    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"{self.name} received notification :\n Stock price is {price}")


class Stock:

    def __init__(self):
        self.price = 0
        self.observers = []


    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        print(f"{observer.name} has unsubscribed..." )
        self.observers.remove(observer)
        print("-" * 60)

    def notify(self):
        for observer in self.observers:
            observer.update(self.price)

    def set_price(self, price):
        self.price = price

        print("-" * 60)
        print(f"Stock price changed to {price}")
        print("-" * 60)
        self.notify()

stock = Stock()

user1 = User("Steve")
user2 = User("Kenith")
user3 = User("Richard")
user4 = User("Peter")
user5 = User("Kennedy")


stock.subscribe(user1)
stock.subscribe(user2)
stock.subscribe(user3)
stock.subscribe(user5)
stock.subscribe(user4)

stock.set_price(230)

stock.unsubscribe(user4)

stock.set_price(100)
