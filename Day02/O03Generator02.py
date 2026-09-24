def my_generator():
    n = 1
    print("Apple")
    yield n
    n += 9
    print("Orange")
    yield n
    n += 10
    print("Pine")
    yield n

res = my_generator()
print(res)

print(res.__next__())     # next(res)
print("Process the data.....")

print(next(res))
print("Process the data.....")

print(next(res))

print("-" * 60)

def get_val():
    for i in range(1, 11):
        yield i

res1 = get_val()
print(next(res1))
print(next(res1))
print(next(res1))
print(next(res1))

print('-' * 60)

for num in get_val():
    print(num, end=" ")
print()
