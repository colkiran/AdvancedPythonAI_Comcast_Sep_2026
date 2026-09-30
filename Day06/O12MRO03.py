
class Base:

    def greet(self):
        print("Base greet....")

class Left(Base):

    def greet(self):
        print("left greet....")
        super().greet()

class Right(Base):

    def greet(self):
        print("Right greet....")
        super().greet()

class Child(Left, Right):

    def greet(self):
        print("Child greet.....")
        super().greet()

Child().greet()
