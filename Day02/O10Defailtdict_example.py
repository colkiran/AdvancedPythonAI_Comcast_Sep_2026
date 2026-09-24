
from collections import defaultdict

transaction = [
    ("cust_1", 250),
    ("cust_2", 400),
    ("cust_1", 100),
    ("cust_3", 500),
    ("cust_2", 200)
]

cust_txns = defaultdict(list)

for cust, amt in transaction:
    cust_txns[cust].append(amt)

for cust, txns in cust_txns.items():
    print(cust, ":", txns)
