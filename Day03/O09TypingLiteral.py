
from typing import Literal

def set_status(status: Literal['online', 'offline', 'busy']) -> None:
    print(f"status is set to {status}")

set_status("online")
set_status("busy")
# warns us stating that 'in a meeting' is not a part of literals mentioned
set_status("in a meeting")
