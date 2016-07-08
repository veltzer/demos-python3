#!/usr/bin/python3

'''
This is an example of how to read data from the user on the console
using the new python3 'input' function.

Notice that:
- return type of 'input' is a string.
- you can convert it to 'int' or 'float' using regular contructors
but there is a chance that they will throw an exception.
- at the end of the string given to 'raw_input' you *do* need a space since
raw input prints to the screen * exactly * what you give it...
- this example will not work in python3 since 'raw_input' got renamed to 'input'
'''

text = input('please give me a number: ')
print('type returned from input is', type(text))
print('value returned from input is', text)
print('converting to int')
val = int(text)
print('new value is', val)
print('new value type is', type(val))
