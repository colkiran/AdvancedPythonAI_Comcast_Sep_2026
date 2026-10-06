
import  multiprocessing as mp

def square(lst, q):
    for n in lst:
        q.put(n * n)

def print_squares(q):

    print("Queue elements...")
    while not q.empty():
        print(q.get(), end=" ")

    print("\nQueue is empty....")

if __name__ == '__main__':
    mylist = list(range(1, 6))

    q = mp.Queue()

    p1 = mp.Process(target=square, args=(mylist, q))
    p2 = mp.Process(target=print_squares, args=(q, ))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
