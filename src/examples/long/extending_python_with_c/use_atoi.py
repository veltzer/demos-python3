#!/usr/bin/python3

'''
the sys.path.append in the next section is needed since we didn't 'properly'
install the module to /usr/share/python.
If we had done this this would not have been neccessary.
'''

import sys # for path
sys.path.append('build/lib.linux-i686-2.7')

import atoi # for atoi

print(atoi.atoi('-7.6'))
