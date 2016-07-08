#!/usr/bin/python3

'''
A program that shows you how to get the size of the terminal.

A clear winner in terms of performance is the ioctl(2) one.

References:
http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
'''

import os  # for popen, environ
import fcntl  # for ioctl
import struct  # for unpack, pack
import termios  # for TIOCGWINSZ
import time  # for time


def terminal_size1():
    h, w, hp, wp = struct.unpack('HHHH',
                                 fcntl.ioctl(0, termios.TIOCGWINSZ,
                                             struct.pack('HHHH', 0, 0, 0, 0)),
                                 )
    return w, h


def terminal_size2():
    ret = os.popen('stty size', 'r').read().split()
    return int(ret[1]), int(ret[0])


def terminal_size3():
    x = int(os.popen('tput cols', 'r').read())
    y = int(os.popen('tput lines', 'r').read())
    return x, y


def terminal_size4():
    d = dict()
    for tc_entry in os.environ['TERMCAP'].split(':'):
        if tc_entry.find('#') != -1:
            key, val = tc_entry.split('#')
            d[key] = val
    return int(d['co']), int(d['li'])
# this function does not work since LINES and COLUMNS are not exported


def terminal_size5():
    x = int(os.environ['LINES'])
    y = int(os.environ['COLUMNS'])
    return x, y

print(terminal_size1())
print(terminal_size2())
print(terminal_size3())
print(terminal_size4())
# print(terminal_size5())

# lets compare performance
count = 1000


def do1():
    for x in range(count):
        terminal_size1()


def do2():
    for x in range(count):
        terminal_size2()


def do3():
    for x in range(count):
        terminal_size3()


def do4():
    for x in range(count):
        terminal_size4()


def do5():
    for x in range(count):
        terminal_size5()


def time_it(f, desc):
    time_before = time.time()
    f()
    time_after = time.time()
    print('time taken for {desc}: {diff:.3f} seconds'.format(
        diff=time_after - time_before,
            desc=desc,
    ))
time_it(do1, 'ioctl')
time_it(do2, 'stty')
time_it(do3, 'tput')
time_it(do4, 'TERMCAP')
# time_it(do5, 'LINES/COLUMNS')
