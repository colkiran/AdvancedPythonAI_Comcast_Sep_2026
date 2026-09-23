
def fun(a,  b):
    print("Hello World")
    # print(f"{a + b}")
    return a + b

res = fun(10, 20)
print(f"res :{res}")

print("-" * 60)

# arguments will be stored in a tuple
def fun1(*num):
    print(num)

fun1()
fun1(10)
fun1(10, 20)
fun1(10, 20, 30)

print("-" * 60)

# arguments will be stored in a dictionary
def player_info(**details):
    # print(details)
    for k, v in details.items():
        print(k, "=>", v)


player_info(name="Virat", age=38, runs=135, oppn="Australia")

print("-" * 60)

def fun2():
    print("Fun2 called.....")

    def fun3():
        print("Fun3 called....")

    fun3()  # call funtion fun3

    print("fun2 continues")

fun2()





