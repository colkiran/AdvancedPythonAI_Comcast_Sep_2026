import cProfile

def slow_function():
    total = 0
    for i in range(10 ** 6):
        total += i
    return total

def fast_function():
    return sum(range(10 ** 6))

def main():
    slow_function()
    fast_function()

cProfile.run("main()")
