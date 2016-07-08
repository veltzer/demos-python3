#!/usr/bin/python3

'''
Examples of constructors in python.
You must accept at least one argument in a constructor in order for it
to count as a constructor. You can also write a 'varargs' constructor.
Errors for not having the right method occur at runtime and not at
compile time. Because python does not have overloading then if you
do decide to write an __init__ method you have to write it well in
order to avoid a runtime error.
'''


class A:

    def __init__():
        print('in A constructor')


class B:

    def __init__(self):
        print('in B constructor')


class C:

    def __init__(self, arg1, arg2):
        print('in C constructor')


class D:

    def __init__(self, * args):
        print('in C constructor')

try:
    a = A()
except TypeError:
    print('oh,no. Cant construct an object. Must pass self')
b = B()
c = C()
d = D()
