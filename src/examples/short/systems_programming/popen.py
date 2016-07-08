#!/usr/bin/python3

'''
This example shows how to call popen and get the return text.
'''

import os  # for popen2

(pin, pout) = os.popen2(['ls', '-l'])
for number, line in enumerate(pout):
    print(number, line)
