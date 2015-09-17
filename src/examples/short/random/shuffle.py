#!/usr/bin/python3

'''
This example shows how to shuffle a list in python
'''

import random  # for seed, shuffle
# for deterministic behaviour
#random.seed(7)
l = list(range(1, 10))
random.shuffle(l)
print(l)
