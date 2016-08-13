#!/usr/bin/python3

'''
This example explores how best to catenate strings in python.

The results are surprising.
It seems the + operator is the quickest
Join has pretty good performance.
'''

import timeit  # for timeit

x='abc'
y='def'
def concat1():
    z=x+y
    return z
def concat2():
    z = "%s%s" % (x, y) 
    return z 
def concat3(): 
    z = "{}{}".format(x, y) 
    return z 
def concat4(): 
    z = "{0}{1}".format(x, y) 
    return z
def concat5(): 
    return ''.join([x,y])

number=1000000

print('+ operator', timeit.timeit(concat1, number=number))
print('%s%s', timeit.timeit(concat2, number=number))
print('{}{}', timeit.timeit(concat3, number=number))
print('{0}{1}', timeit.timeit(concat4, number=number))
print('join', timeit.timeit(concat5, number=number))
