#!/usr/bin/python3

'''
This example explores corret function order in the source code.

This means that a function cannot be used until after it has been defined.
'''

# this is wrong
# foo()


def foo():
    print('this is foo')
    bar()

# this is wrong...
# foo()


def bar():
    print('this is bar')

foo()
del bar
foo()
