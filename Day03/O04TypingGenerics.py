
from typing import List, Dict

def process(data: List[int]) -> Dict[str, int]:
    return{"sum": sum(data), "count": len(data)}

res = process([10, 20, 30, 40])
print(f"res :{res}")
