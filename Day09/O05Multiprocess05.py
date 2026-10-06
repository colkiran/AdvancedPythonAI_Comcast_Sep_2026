import multiprocessing as mp

def sender(conn, msgs):

    for msg in msgs:
        conn.send(msg)
        print("Message sent :{}".format(msg))
    conn.close()

def receiver(conn):

    while True:
        msg = conn.recv()
        if msg == "END":
            break
        print("Message Recieved :{}".format(msg))

if __name__ == '__main__':
    msgs = ["Hello", "Hai", "Good Day", "Thank you", "END"]

    parent_conn, child_conn = mp.Pipe()

    p1 = mp.Process(target=sender, args=(parent_conn, msgs))
    p2 = mp.Process(target=receiver, args=(child_conn, ))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
