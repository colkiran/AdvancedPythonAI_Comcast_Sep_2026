
from typing import Protocol

class Flyer(Protocol):
    def fly(self) -> None: ...


class Bird:
    def fly(self) -> None:
        print("Flying high.....")

class Fish:
    def eat(self) -> None:
        print("Fish eats to survive....")

def make_it_fly(entity: Flyer):
    entity.fly()

bird = Bird()
fish = Fish()
make_it_fly(bird)

# does not work since it is not of type flyer protocol
# make_it_fly(fish)
