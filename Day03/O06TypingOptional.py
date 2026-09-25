"""
Optional[X] is a shorthand of Union[X, None]
"""

from typing import Optional

def find_user(id: int) -> Optional[str]:
    return "Success" if id == 1 else None

print(find_user(1))
print(find_user(2))
