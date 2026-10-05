from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"Task starting {name}")
    time.sleep(2)
    print(f"Task completed {name}")

# create a pool of threads
with ThreadPoolExecutor(max_workers=3) as executor:
    tasks = [executor.submit(task, f"task - {i}") for i in range(5)]

print("All tasks submitted....")