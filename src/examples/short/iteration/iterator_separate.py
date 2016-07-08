#!/usr/bin/python3

'''
This is an example of building an iterator. In this case the iterator
object returned is a different object than the one which is being iterated.
This is a nicer design.
'''


class RevIter:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

'''
Iterator for looping over a sequence backwards
'''


class Reverse:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return RevIter(self.data)

'''
And now lets use the iterator...
'''
l = range(7)
for x in Reverse(l):
    print(x)

'''
notice that Reverse(x) is NOT an iterator,at least by pythons understanding of it.
Compare to pythons own reversed(x) implementation which does return an iterator...
'''
r = Reverse(l)
print(type(r))
r2 = reversed(l)
print(type(r2))
print(dir(r2))
