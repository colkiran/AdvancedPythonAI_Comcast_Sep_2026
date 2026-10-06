import multiprocessing as mp

def print_records(recs):

    for rec in recs:
        print("Name: {0}\nScore: {1}\n".format(rec[0], rec[1]))

def insert_record(rec, recs):
    recs.append(rec)
    print("New record added.....")


if __name__ == '__main__':
    with mp.Manager() as mgr:
        recs = mgr.list([('apple', 285), ('orange', 150), ('Mango', 225)])
        new_rec = ('grapes', 175)

        p1 = mp.Process(target=insert_record, args=(new_rec, recs))
        p2 = mp.Process(target=print_records, args=(recs, ))

        p1.start()
        p1.join()

        p2.start()
        p2.join()

