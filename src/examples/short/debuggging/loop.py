#!/usr/bin/python3

'''
This is a small example which does not directly use the debugger
so that you could debug it from the command line like so:
pdb src/examples/short/debuggging/loop.py
'''


def calc():
    i = 0
    sum = 0
    while True:
        sum = sum + i
        i = i + 1

calc()
