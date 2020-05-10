from multiprocessing import Process
import os
import time
from multiprocessing import Pool

def func():
    while True:
        print("i am func")
        time.sleep(1)

if __name__ == "main":
    process = Process(target = func)
    process.start()

    pool = Pool(5)

    pool.apply_async(func)
    pool.close()
    pool.join()
