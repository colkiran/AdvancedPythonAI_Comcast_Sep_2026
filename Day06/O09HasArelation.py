
# instead of inheritance classes can be built by combining other classes

class Engine:
    def start(self):
        print("Engine starts.....")

class Car:
    def __init__(self):
        self.engine = Engine()      #composition

    def drive(self):
        self.engine.start()
        print("Car drives")

car = Car()
car.drive()
