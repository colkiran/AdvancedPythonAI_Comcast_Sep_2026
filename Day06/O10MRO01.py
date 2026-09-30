
class A:

    def greet(self):
        print("hello from A")

class B(A):

    def greet(self):
        print("hello from B")

obj = B()
obj.greet()
print("-" * 60)
print(B.__mro__)
