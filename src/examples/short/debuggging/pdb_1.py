#!/usr/bin/python3

'''
This is an example of how to debug a python application
just run this application and you will enter debug mode
as soon as you start the trace...
'''

import pdb  # for set_trace

# This will make you enter debug start right from the start...
# pdb.set_trace()


def calc():
    i = 0
    sum = 0
    while True:
        sum = sum + i
        if i == 600:
            pdb.set_trace()
        i = i + 1

calc()
