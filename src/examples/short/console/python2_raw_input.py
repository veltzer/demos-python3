#!/usr/bin/python3

'''
This is an example of how to read data from the user on the console
in python2 using the 'raw_input' function.

Notice that:
- return type of 'raw_input' is a string.
- you can convert it to 'int' or 'float' using regular contructors
but there is a chance that they will throw an exception.
- at the end of the string given to 'raw_input' you *do* need a space since
raw input prints to the screen * exactly * what you give it...
- this example will not work in python3 since 'raw_input' got renamed to 'input'
'''

text = raw_input('please give me a number: ')
print(type(text))
val = int(text)
print('val is', val)
print('type(val) is', type(val))
