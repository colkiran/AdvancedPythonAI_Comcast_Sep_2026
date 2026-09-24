
print(sum([x ** 2 for x in range(11)]))     # List Comprehension
print(sum((x ** 2 for x in range(11))))     # generator

print('-' * 60)
from sys import getsizeof
values01 = [x ** 2 for x in range(10000)]
print(f"Comprehension size of lst :{getsizeof(values01)}")

values02 = (x ** 2 for x in range(10000))
print(f"Generator size of lst     :{getsizeof(values02)}")

print('-' * 60)
values03 = (x for x in range(10))

for num in values03:
    print(num)

print('-' * 60)

l = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"l :{l}")
print(type(l))

itrObj = iter(l)

while(True):
    try:
        elem = next(itrObj)
        print(elem)
    except StopIteration:
        break
