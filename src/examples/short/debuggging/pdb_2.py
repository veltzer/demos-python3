#!/usr/bin/python3

'''
This is an example of debugging python with pdb.
'''

import pdb  # for set_trace

pdb.set_trace()


def calc():
    i = 0
    sum = 0
    while True:
        sum = sum + i
        i = i + 1

calc()
