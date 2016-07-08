#!/usr/bin/python3

'''
This example demonstrates how to analyze the return code of a child process.
'''

import os  # for system

ret = os.system('ls -l >/dev/null')
print(ret)
ret = os.system('ls -l sdfsdf >/dev/null')
print(ret)
