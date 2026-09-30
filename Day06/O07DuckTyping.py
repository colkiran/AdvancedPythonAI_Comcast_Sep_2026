
class Duck:
    def quack(self):
        print("quack quack")

class Person:
    def quack(self):
        print("I can quack like a duck")

def make_it_quack(entity):
    entity.quack()

duck = Duck()
human = Person()

make_it_quack(duck)
make_it_quack(human)
