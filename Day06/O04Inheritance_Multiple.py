
class Animal:

    def __init__(self):
        self.a = 10
        print("Animal Ctor......")

    def eat(self):
        print("Animals Eat.....")

    def fun(self):
        print("Fun method of Animal class.....")
class Person:
    def __init__(self):
        self.p = 20
        print("Person Ctor.....")

    def talk(self):
        print("Person talks........")

    def fun(self):
        print("fun method of class Person....")
class Girl(Animal, Person):

    def __init__(self):
        self.g = 30
        super().__init__()
        Person.__init__(self)
        print("Girl Ctor......")


maria = Girl()
maria.talk()
maria.eat()

print("-" * 60)
maria.fun()         # which fun method will call and why

print("-" * 60)
print(maria.__dict__)
