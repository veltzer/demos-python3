#!/usr/bin/python3

'''
This example is similar to while(<>) in perl which processes input
both from standard input and from command line arguments.
'''

import fileinput # for input

for line in fileinput.input():
    line = line.rstrip()
    print(line)
