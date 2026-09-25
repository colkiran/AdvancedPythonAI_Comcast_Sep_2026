from typing import List

def greet(names: List[str]) -> str:
    # return f"Hello {', '.join([str(name) for name in names])}"
    return f"Hello {', '.join(names)}"

res = greet(['Sachin', "Virat"])
print(res)
