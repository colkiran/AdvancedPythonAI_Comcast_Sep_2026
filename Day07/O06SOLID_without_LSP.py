
class Bird:

    def fly(self):
        return 'Flying high in the sky.....'

class Parrot(Bird):

    def fly(self):
        return "Parrot is flying high....."

class Penguin(Bird):
    # Violation LSP: Pengui cannot fly but base class expects all birds to fly
    def fly(self):
        return "Penguin is flying high....."


def make_bird_fly(bird: Bird):
    print(bird.fly())

make_bird_fly(Parrot())
make_bird_fly(Penguin())