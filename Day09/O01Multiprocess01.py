import multiprocessing as mp
import os


def worker1():
    print("ID of process worker1 : {}".format(os.getpid()))

def worker2():
    print("ID of process worker2 : {}".format(os.getpid()))

if __name__ == '__main__':
    print("ID of main process is {}".format(os.getpid()))

    p1 = mp.Process(target=worker1)
    p2 = mp.Process(target=worker2)

    p1.start()
    p2.start()

    print("ID of P1 :{}".format(p1.pid))
    print("ID of P2 :{}".format(p2.pid))

    p1.join()
    p2.join()

    print("Process p1 is alive :{}".format(p1.is_alive()))
    print("Process p2 is alive :{}".format(p2.is_alive()))
