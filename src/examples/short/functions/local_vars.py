#!/usr/bin/python3


def myfunc(y):
    print(locals())
    print(x)
    x = 5
    print(x)
    print(locals())

x = 7
myfunc(9)
print(x)
