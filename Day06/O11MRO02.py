class A:

    def greet(self):
        print('Hello from A')

    def msg(self):
        print("Hai from A")

class B(A):

    def greet(self):
        print("Hello from B")

class C(A):

    def greet(self):
        print("Hello from C")


class D(B, C):
    pass

d = D()
d.greet()
print(D.__mro__)
d.msg()