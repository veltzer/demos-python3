#!/usr/bin/python3

'''
A more complex example involving deferreds.
'''

from twisted.internet import defer
import time

TARGET = 10000


def largeFibonnaciNumber():
    # create a Deferred object to return:
    d = defer.Deferred()

    # calculate the ten thousandth Fibonnaci number
    first = 0
    second = 1
    for i in range(TARGET - 1):
        new = first + second
        first = second
        second = new
        if i % 1000 == 0:
            print('Progress: calculating the {0}th Fibonnaci number'.format(i))
    # give the Deferred the answer to pass to the callbacks:
    d.callback(second)
    # return the Deferred with the answer:
    return d

timeBefore = time.time()

# call the function and get our Deferred
d = largeFibonnaciNumber()

timeAfter = time.time()

print(
    'Total time taken for largeFibonnaciNumber call: {0:.3f} seconds'.format(timeAfter - timeBefore))

# add a callback to it to output the number


def printNumber(number):
    print('The %dth Fibonacci number is %d' % (TARGET, number))

print('Adding the callback now.')
d.addCallback(printNumber)
