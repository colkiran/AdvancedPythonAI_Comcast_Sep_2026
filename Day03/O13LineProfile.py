from line_profiler import profile

@profile
def slow_function():
    total = 0
    for i in range(10 ** 6):
        total += i
    return total

slow_function()
