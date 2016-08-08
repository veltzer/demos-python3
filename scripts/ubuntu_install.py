#!/usr/bin/python3

'''
this script will install all the required packages that you need on
ubuntu to compile and work with this package.
'''

import subprocess # for check_call

do_pips=False
opt_python_version='3.5'

packs=[
	# python core
	'python3',
	'python3-doc',
	'python3-examples',
	'python{0}'.format(opt_python_version),
	'python{0}-doc'.format(opt_python_version),
	'python{0}-examples'.format(opt_python_version),
	'python{0}-dev'.format(opt_python_version),
	'python{0}-venv'.format(opt_python_version),

	# iteractive, parallel python
	'ipython',

	# tools for python packaging and upload
	'twine',

	# qt
	'pyqt4-dev-tools',
	'python-qt4',
	'python-qt4-sql',
	'python-qt4-dbus',
	'python3-pyqt4',
	'python3-dbus.mainloop.qt',

	# curses
	'python-newt',
	'python3-newt',
	#'python-dialog',
	'python3-dialog',

	# misc modules
	'python-imdbpy',
	'python-mysql.connector',
	'python3-mysql.connector',
	'python3-progressbar',
	'python-networkx', # tool to create, manipulate and study complex networks documentation
	'python3-networkx', # tool to create, manipulate and study complex networks (Python3)
	'python3-pygraph', # library for working with graphs in Python (Python3)
	'python-yapsy', # simple plugin system for Python applications
	'python-yapsy-doc', # simple plugin system for Python applications doc
	'python3-yapsy', # simple plugin system for Python3 applications
	'python3-pygments', # for syntaxh highlighting

	# debuggers
	'winpdb',
	'pydb',
	'python-pudb',
	'python3-pudb',

	# sphinx
	'python3-sphinx', # documentation generator for Python projects (implemented in Python 3)
	'python3-sphinx-paramlinks', # allows param links in Sphinx function/method descriptions to be linkable
	'python3-sphinxcontrib.programoutput', # insert the output of arbitrary commands into documents Python 3.x
	'python3-sphinxcontrib.spelling', # Sphinx spelling extension (Python 3)
	'python3-sphinxcontrib.youtube', # Sphinx YouTube extension

	# from my own repo
	'templar',
	#'pdmt',

	# notify related packages
	'python-inotifyx',
	'python-notify',
	'python-notify2',
	'python-pyinotify',
	'python-pyinotify-doc',
	'python3-notify2',
	'python3-pyinotify',

	# python and gtk stuff
	'glade',

	# lint and code formatting
	'python-autopep8',

	# pdf creation with python
	'python-pypdf2',
	'python3-pypdf2',
]

pips=[
	'signalfd',
]

args=['sudo','apt-get','install','--assume-yes']
args.extend(packs)
subprocess.check_call(args)

if do_pips:
	for pip in pips:
		args=['sudo', 'pip', 'install', pip]
		subprocess.check_call(args)
		args=['sudo', 'pip3', 'install', pip]
		subprocess.check_call(args)
