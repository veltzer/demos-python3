#!/usr/bin/python3

'''
This example is taken from the following talk:
http://pyvideo.org/video/588/mindblowing-python-gil

Results:
$ python --version
Python 2.7.9
$ ./gil_python2.py
time taken for single thread: 6.288 seconds
time taken for two threads: 9.156 seconds

Conclusions:
In python 2 the gil is pretty awful. It takes 150% of the time of a single thread. Write single threaded code
and avoid the non-efficient locking of the gil.
'''

#
# imports #
#
import threading  # for Thread
import time  # for time

#
# parameters #
#
limit = 100000000

#
# functions #
#


def count(n):
    while n > 0:
        n -= 1

#
# code #
#

# first single thread
time_before = time.time()
count(limit)
count(limit)
time_after = time.time()
print('time taken for single thread: {0:.3f} seconds'.format(
    time_after - time_before,
))

# now two threads
time_before = time.time()
t1 = threading.Thread(target=count, args=(limit,))
t2 = threading.Thread(target=count, args=(limit,))
t1.start()
t2.start()
t1.join()
t2.join()
time_after = time.time()
print('time taken for two threads: {0:.3f} seconds'.format(
    time_after - time_before,
))
