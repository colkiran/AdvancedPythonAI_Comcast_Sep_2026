
# synchronous way of calling (execution)

import time

ST = time.perf_counter()

def doJob():
    print("Executing the job.....")
    time.sleep(2)
    print("Completed executing.....")

doJob()
doJob()
doJob()

ET = time.perf_counter()
print(f"The total time taken to execute the job is {round(ET - ST, 2)}")