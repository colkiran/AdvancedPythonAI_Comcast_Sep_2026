
def fun():
    print("Function fun called....")

    def fun1():
        print("Function fun1 called.....")

    return fun1

fun()

print("-" * 60)
fun()()     # calls fun1

print("-" * 60)
fun1_ref = fun()
fun1_ref()
