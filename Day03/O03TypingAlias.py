from typing import TypeAlias
Vector: TypeAlias = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

res = scale(2.0, [1.0, 2.0, 3.0])
print(res)