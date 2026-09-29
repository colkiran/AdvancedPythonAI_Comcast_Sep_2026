
import shelve

with shelve.open("mydata") as DB:
    # store data
    DB["user"] = {"name": "Steve", "age": 32}
    DB["numbers"] = list(range(1, 6))

    # reopen and read data
with shelve.open("mydata") as DB:
    print(DB["user"])
    print(DB["numbers"])
