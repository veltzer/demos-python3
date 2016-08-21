#!/usr/bin/python2

'''
This is an example of a weird pattern in OO python
in which the local attributes of an
instance get populated from the global (class based)
ones.
'''

from abc import ABCMeta

class MyClass(object):
    __metaclass__ = ABCMeta
    foo=14;

    def __init__(self, foo):
        if foo:
            self.foo=foo
        else:
            self.foo=self.foo

    def do_print(self):
        print 'foo is', self.foo

''' Lets show how we use our object... '''
b = MyClass(15)
b.do_print()
b = MyClass(16)
b.do_print()