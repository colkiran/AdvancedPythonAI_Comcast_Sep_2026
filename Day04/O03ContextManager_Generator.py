
from contextlib import contextmanager

@contextmanager
def batch_reader(filename, batch_size=50):
    """
    context manager that yields 50 recs at a time from a file
    Each yield returns a list of batch_size recs
    """

    F = open(filename, "r", encoding="utf-8")
    try:
        batch = []
        for line in F:
            batch.append(line.split())
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch
    finally:
        F.close()

with batch_reader("employeeData.csv", batch_size=1000) as R:
    for batch in R:
        print("batch size :", len(batch))
        for rec in batch:
            print(rec)
        print("-" * 60)






