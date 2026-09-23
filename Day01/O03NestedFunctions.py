
def fun(x):
    print(f"x :{x}")

    def fun1(y):
        nonlocal x
        print(f"y :{y}")
        print(f"before Inside fun1 x: {x}")
        x += 100
        print(f"after Inside fun1 x: {x}")


    return fun1

ref = fun(100)
ref(200)

print("-" * 60)

x = 100
def fun2():
    global x
    print("hello world")
    print(f"x :{x}")
    x = 500         # local variable
    print(f"x :{x}")

fun2()
print(f"Afer the function call x: {x}")

print("-" * 60)
# variables declared inside the function cannot be accessed outside the function
# they are local variable with lexical scope

def fun3():
    print("hello world")
    z = 250
    print(f"z :{z}")

fun3()
print(f"z :{z}")