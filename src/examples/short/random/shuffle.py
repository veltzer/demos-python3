#!/usr/bin/python3

'''
This example shows how to shuffle a list in python

References:
http://stackoverflow.com/questions/2124347/how-to-generate-permutations-of-array-in-python
'''

import random  # for seed, shuffle
# for deterministic behaviour
#random.seed(7)
l = list(range(1, 10))
random.shuffle(l)
print(l)
