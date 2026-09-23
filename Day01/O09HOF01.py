
def sum(x, y):
    return x + y

def diff(x, y):
    return x - y


def log_details(fnc):
    logInfo = "Logging into done....."

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))
        print("-" * 60)

    return innerFun

sumlogger = log_details(sum)
difflogger = log_details(diff)

sumlogger(10, 20)
difflogger(30, 12)







