import time
import os

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
    pid = os.getpid()
    print(f"pid :{pid}")
    time.sleep(2)

# cProfile.run("main()")
if __name__ == '__main__':
    main()


"""
Total samples: 1000
%   Function
80% slow_function
15% fast_function
5%  time.sleep
"""