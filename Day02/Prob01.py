def dec1(func):
    def wrapper():
        func()         # calls dec2 wrapper first
        print("~" * 25)
        print("=" * 25)
    return wrapper


def dec2(func):
    def wrapper():
        print("-" * 25)
        print("*" * 25)
        func()         # calls original fun
    return wrapper


@dec1
@dec2
def fun():
    print("Hello World")


fun()