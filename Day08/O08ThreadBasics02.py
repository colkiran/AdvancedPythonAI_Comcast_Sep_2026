
# asynchronous Execution of code

import threading
import time

ST = time.perf_counter()

def do_job():
    print(f"Starting thread ..{threading.current_thread().name}")
    time.sleep(2)
    print(f"Just woke up.....{threading.current_thread().name}")

thrd1 = threading.Thread(target=do_job, name = "trd1")
thrd2 = threading.Thread(target=do_job, name = 'trd2')
thrd3 = threading.Thread(target=do_job, name = 'trd3')

thrd1.start()
thrd2.start()
thrd3.start()

thrd1.join()
thrd2.join()
thrd3.join()

ET = time.perf_counter()

print(f"The totsl time taken to execute is :{round(ET - ST, 2)}")