#!/usr/bin/python3

'''
Question: what does this function output ?

Answer: exception.
'''


def my_mistery_function():
    # global g
    print(g)
    if False:
        g += 17
    print(g)

g = 4
my_mistery_function()
print(g)
