#!/usr/bin/python3

'''
This example shows how to use math.inf

References:
http://stackoverflow.com/questions/7781260/how-can-i-represent-an-infinite-number-in-python
'''

import math # for inf

test = math.inf

print(test)
print(test > 1)
print(test > 10000)
test -= 1000
print(test)
print(test > 7)
