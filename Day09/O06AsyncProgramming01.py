
import asyncio

async def task1():
    print("Task 1 started....")
    # simulates I/O work
    await asyncio.sleep(2)
    print("Task 1 finished.....")

async def task2():
    print("Task 2 started....")
    await asyncio.sleep(2)
    print("Task 2 finished......")

async def main():
    # Schedule tasks to run concurrently
    await asyncio.gather(task1(), task2())

# event loop manages execution by switching between tasks efficiently
asyncio.run(main())

