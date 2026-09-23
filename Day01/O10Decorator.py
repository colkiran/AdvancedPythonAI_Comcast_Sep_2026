
def funlogger(fnc):
    def helper(a, b):
        print("My info logged into a service.....")
        res = fnc(a, b)         # call back
        print("My info logger chanel closed.....")
        return res
    return helper

@funlogger
def sum(x, y):
    return x + y

@funlogger
def diff(x, y):
    return x - y


# sum = funlogger(sum)
print(sum(35, 69))

print("-" * 60)
print(diff(74, 28))