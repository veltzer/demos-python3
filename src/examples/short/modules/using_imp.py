#!/usr/bin/python3

'''
Demo to show the usage of the imp module in python
This clearly shows that you can reload any module into any name space using
the imp module.
'''

import imp # for load_source

imp.load_source('__main__', 'using_imp_one.py')
print('add(2,2) is', add(2, 2))
imp.load_source('__main__', 'using_imp_two.py')
print('add(2,2) is', add(2, 2))

import math
print('math.sin(0.5) is', math.sin(0.5))
imp.load_source('math', 'using_imp_three.py')
print('math.sin(0.5) is', math.sin(0.5))
