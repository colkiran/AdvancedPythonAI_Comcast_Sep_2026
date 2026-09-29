
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fn, ln, age):
        print("factory......")
        return cls(f"{fn} {ln}", age)    # call the constructor


player1 = Player("Rohit", 37)
player1.get_details()

print("-" * 60)
player2 = Player.CreatePlayer("Rohit", "Sharma", 37)
player2.get_details()