#!/usr/bin/python3

'''
This example explores the 'input' function in python2
which is different from the 'input' function in python3.

Notes:
- 'input' in python2 does an 'eval' on the input from
the console.
- this makes this function inherently unsafe.
- this also make it unpredictable (try to put a float,
or a double or whatever).
- I don't like this function in python2.
'''

text = input('please give me a number: ')
print('type of return from input is', type(text))
print('value returned from input is', text)
