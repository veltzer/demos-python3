#!/usr/bin/python3

'''
An example showing the different ways to create dicts
'''

# simplest way, build in the language syntax
d1 = {}
# constructor
d2 = dict()
# copy
d3 = dict(d1)
# comprehension
d4 = {x: x * x for x in range(5)}

print(d1)
print(d2)
print(d3)
print(d4)
