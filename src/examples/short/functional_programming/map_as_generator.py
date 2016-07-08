#!/usr/bin/python3
#!/usr/bin/python3

'''
This example shows that map knows when it is used as a generator and behaves differently
in that context (not generating the full list).
You need python 3.0 to see this in action,in versions before 3 it actually creates the
list. In version 3 the first output will not work since it returns a generator
'''


def my_gen():
    for i in range(10):
        # print('my_gen')
        yield i ** 2


def plus1(x):
    # print('plus1')
    return x + 1
print(map(plus1, my_gen()))
for x in map(plus1, my_gen()):
    pass
    # print(x)
