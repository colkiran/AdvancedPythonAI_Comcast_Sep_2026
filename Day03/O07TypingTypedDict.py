
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    active: bool

user: User = {'id': 10, 'name': 'Micheal', 'active': True}
print(f"Name :{user['name']}")
print(f"Active :{user['active']}")
