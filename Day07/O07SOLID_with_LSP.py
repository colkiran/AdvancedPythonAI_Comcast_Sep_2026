
from abc import ABC, abstractmethod

class Bird(ABC):

    @abstractmethod
    def move(self):
        pass

class FlyableBird(Bird):
    def move(self):
        print("Flying high in the sky")

class NonFlyableBird(Bird):
    def move(self):
        print("Can walk or swim")

class Parrot(FlyableBird):
    def move(self):
        return "Sparrow is flying"

class Penguin(NonFlyableBird):
    def move(self):
        return "Penguin is swimming"

def make_bird_move(bird: Bird):
    print(bird.move())

make_bird_move(Parrot())
make_bird_move(Penguin())
