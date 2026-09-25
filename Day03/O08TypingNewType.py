
from typing import NewType

UserId = NewType("UserId", int)

def get_user(user_id: UserId) -> str:
    return f"User :{user_id}"

uid = UserId(101)
print(get_user(uid))

# error because it's not of type UserId
print(get_user(101))