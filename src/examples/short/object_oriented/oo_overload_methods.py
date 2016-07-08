#!/usr/bin/python3

'''
This example plainly shows that you cannot have two methods in a class by the same
name. This is true for constructors as well as for regular methods.
'''


class A:

    def __init__(self, val):
        self.__privar = val

    def __init__(self):
        self.__privar = 5

    def sayHello(self):
        print(self.__privar, 'hello')

    def sayHello(self, name):
        print(self.__privar, 'hello', name)

try:
    a = A(5)
except TypeError:
    print('oops,got an error')
    print('the no argument version of the constructor does not exist...')
# this will pass without an exception...
a = A()
try:
    a.sayHello()
except TypeError:
    print('oops,got an error')
    print(
        'the no argument version of the method \'sayHello\' does not exist...')
a.sayHello('mark')
