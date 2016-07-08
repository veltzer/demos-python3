#!/usr/bin/python3

'''
A demo of how warnings work in python.
'''

import warnings  # for warn, simplefilter


def fxn():
    print('in the function')
    # warnings.warn('deprecated', DeprecationWarning)
    # warnings.warn('this is a warning', Warning)
    warnings.warn('this is a problem')

# with warnings.catch_warnings():
# warnings.simplefilter('ignore')
# warnings.filterwarnings('error')
warnings.filterwarnings('ignore')
fxn()
warnings.filterwarnings('error')
# warnings.resetwarnings()
fxn()
# warnings.warn('this is a problem')
fxn()
