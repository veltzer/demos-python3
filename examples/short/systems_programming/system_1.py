#!/usr/bin/python

"""
This example demonstrates the use of the 'exec' family of functions. Notice that after
you call them you are no longer running (your executable get replaced or rather the python
virtual machine gets replaced...).

	Mark Veltzer <mark@veltzer.net>
"""
import os

r=os.system("ls -l")
print("Im still here")
os.execl("/bin/ls")
print("Where am I?")
