#!/usr/bin/python3

'''
This example iterates two or more containers at the same time.

Notes:
- if the two lists are not of the same length then zip iterates
until the shorter one (see second example).

TODO:
- show how to iterate two containers in sequence instead of simultaneously.
'''

ll1 = [1, 2, 3, 4, 5]
ll2 = [10, 11, 12, 13, 14]
ll3 = [20, 21, 22, 23, 24]

for (l1, l2, l3) in zip(ll1, ll2, ll3):
    print(l1, l2, l3)

lll1 = [1, 2, 3]
lll2 = [4, 5]

for (x, y) in zip(lll1, lll2):
    print(x, y)
