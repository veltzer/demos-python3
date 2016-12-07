#!/usr/bin/python3

"""
This example shows what happens when you use multiprocessing
and throw exceptions from the processes.

THIS IS REALLY BAD! NOTHING HAPPENS!
Solution: ALWAYS pass the 'error_callback' parameter with a function
that prints the exceptions.
"""

import multiprocessing  # for cpu_count
import time  # for sleep

def sleep_a_little(num):
    time.sleep(1)
    raise ValueError('this is bad '+str(num))

def print_exception(e):
    print('exception happened', e)

pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
for i in range(10):
    pool.apply_async(sleep_a_little, [i], error_callback=print_exception)
pool.close()
pool.join()