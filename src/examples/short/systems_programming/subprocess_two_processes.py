#!/usr/bin/python3

'''
This example shows how to create two processes in python that communicate via a pipe.
'''

'''
This function receives two lists to serve as the new processes
'''
import subprocess
import sys


def system_pipe(list1, list2, getOutput=False, getError=False):
    pr1 = subprocess.Popen(
        list1,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
    )
    pr2 = subprocess.Popen(
        list2,
            stdin=pr1.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
    )
    # the order of the following two lines don't matter but we do need
    # to wait for the two processes to be over...
    status = pr1.wait()
    (s_output2, s_error2) = pr2.communicate()
    if status:
        raise ValueError('error in executing', list1)
    status = pr2.returncode
    if status:
        raise ValueError('error in executing', list2, s_error2)
    # return s_output1,s_error1,s_output2,s_error2
    return s_output2, s_error2

try:
    # test error in first command
    print(system_pipe(
        ['ls', '-l', 'foo'],
            ['wc', '-l'],
    ))
except ValueError as e:
    print('ok, got error for first command', e)
try:
    # test error in second command
    print(system_pipe(
        ['ls', '-l'],
            ['wc', '-l', '--stam'],
    ))
except ValueError as e:
    print('ok, got error for second command', e)
# test output
print(system_pipe(
    ['ls', '-l'],
        ['wc', '-l'],
))
