#!/usr/bin/python3

'''
This is an example of how to use pythons built-in ConfigParser for python2.
'''

import os.path  # for expanduser
import ConfigParser  # for ConfigParser

inifile = os.path.expanduser('~/.github.ini')
config = ConfigParser.ConfigParser()
config.read(inifile)
opt_login = config.get('github', 'login')
opt_pass = config.get('github', 'pass')
print('opt_login is [{0}]'.format(opt_login))
print('opt_pass is [{0}]'.format(opt_pass))
