
l1 = list(range(1,6))
print(f"l1 :{l1}")

l2 = l1             # shallow copy
print(f"L2 :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"l2 :{l2}")
print(f"l1 :{l1}")

print("*" * 60)
print("*" * 60)

print("copy".center(60, "-"))
l3 = [1, 2, 3, 4, 5]
print(f'l3 :{l3}')

l4 = l3.copy()          # deep copy
print(f"l4 :{l4}")

l4.extend([6, 7, 8, 9])
print(f"l4 :{l4}")
print(f"l3 :{l3}")

print("*" * 60)
print("*" * 60)

print("copy".center(60, "-"))

l5 = [1, 2, 3, [10, 20, 30], 4, 5]
print(f"l5 :{l5}")

l6 = l5.copy()
print(f"l6 :{l6}")

l6[3].append(40)
l6[3].append(50)

print(f"l6 :{l6}")
print(f"l5 :{l5}")

print("*" * 60)
print("*" * 60)

print("deepcopy".center(60, "-"))
from copy import deepcopy

l7 = [2, 4, [1, 2, 3], 6, 8, 10]
print(f"l7 :{l7}")

l8 = deepcopy(l7)
print(f"l8 :{l8}")

l8[2].extend([4, 5])
print(f"l8 :{l8}")
print(f"l7 :{l7}")

# same principle works on a dictionary also