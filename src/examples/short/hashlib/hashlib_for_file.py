#!/usr/bin/python3

'''
This is an example of how to use the python builtin 'hashlib' module
for calculating hash functions of file content.

References:
http://pythoncentral.io/hashing-files-with-python/
'''

import hashlib # for new
import subprocess # for check_output

def hexdigest(filename, algo):
	BLOCKSIZE = 65536
	hasher = hashlib.new(algo)
	with open(filename, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(BLOCKSIZE)
	return hasher.hexdigest()

print(hashlib.algorithms_available)
print(hexdigest('/etc/passwd', 'sha512'))
print(subprocess.check_output(['sha512sum', '/etc/passwd']))
