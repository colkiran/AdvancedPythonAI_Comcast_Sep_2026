
import multiprocessing as mp
import os

result = []

def squares(lst):
    global result
    print('Hello World')
    for num in lst:
        result.append(num * num)
    print("Result in p1 {} is {}".format(os.getpid(), result))

if __name__ == '__main__':
    mylst = [1, 2, 3, 4, 5]

    p1 = mp.Process(target=squares, args=(mylst, ))
    p1.start()
    p1.join()

    print("Result in the main process :{}".format(result))

