
from typing import Annotated
import math

def calculate_area(radius: Annotated[float, 'must be positive']) -> float:
    return math.pi * radius * radius

print(calculate_area(5.0))
print(calculate_area(2.8))

print(calculate_area(1.2))