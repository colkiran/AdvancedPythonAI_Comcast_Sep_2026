
from typing import Union

def stringify(value :Union[int, float, str]) -> str:
    return str(value)

res = stringify(100)
print(res)
print(type(res))

print("-" * 60)

res = stringify(8.75)
print(res)
print(type(res))

print("-" * 60)
res = stringify("Hello")
print(res)
print(type(res))

