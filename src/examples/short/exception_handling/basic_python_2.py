#!/usr/bin/python3

'''
Example code for raising an exception,catching it and executing finally code in python.

Notes:
- note the difference between python3 and python2 syntax for exception handling. In
python 2 the line: 'except ValueError as e' would turn into 'except ValueError,e'
'''

try:
    raise ValueError('hello')
# this next line catches only ValueError exceptions, logs and throws them
# back...
except ValueError as e:
    print('in except', e)
    raise e
finally:
    print('finally is here')
