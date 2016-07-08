#!/usr/bin/python3

'''
setup.py file for SWIG atoi
'''

import distutils.core # for setup, Extension

atoi_module = distutils.core.Extension('_atoi',
	sources=['atoi_wrap.c'],
)
distutils.core.setup(
    name='atoi',
        version='0.1',
        author='SWIG Docs',
        description='''Simple swig atoi from docs''',
        ext_modules=[atoi_module],
        py_modules=['atoi'],
)
