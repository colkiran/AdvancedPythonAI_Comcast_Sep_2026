
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Division by zero not allowed....")
    return a / b

divide(10, 2)
divide(4, 0)
