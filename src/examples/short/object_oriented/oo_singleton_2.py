#!/usr/bin/python3

'''
This is an improvement on the previous singleton example.
This time we make the singleton access method a static method
and not just a global function.

Notes:
- In this example we do not protect against concurrent access.
'''


class A:
    instance = None

    def __init__(self):
        if A.instance is not None:
            raise Exception('you called the constructor twice!!')
        else:
            # constructor code goes here
            print('in A constructor')
            self.my_attribute = 'value'

    #@classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance
    getInstance = classmethod(getInstance)

a1 = A.getInstance()
a2 = A.getInstance()
if a1 is a2:
    print('yes,they are the same instance')
print(a1)
print(a2)
print(dir(a1))
print(dir(a2))
