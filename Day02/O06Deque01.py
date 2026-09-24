
from collections import deque

# create a deque
dq = deque([1, 2, 3, 4, 5])

print(f"dq :{dq}")
print(type(dq))

# Add new elements
dq.append(4)
dq.extend([5, 6, 7])
dq.appendleft(0)
dq.extendleft([-1, -2, -3])

print(f"dq :{dq}")

print("-" * 60)
res = dq.pop()
print(f"res :{res}")

res = dq.popleft()
print(f"res :{res}")

print(f"dq :{dq}")
