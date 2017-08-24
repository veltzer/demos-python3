#!/usr/bin/env python

"""
This example shows that two activations of the gzip library to compress files
actually produce files with different md5 signatures.

The reason for this is the filename, date and compression levels.
You can control this by uding the GzipFile object which has more
parameters. This is not yet demonstrated in this demo.

References:
- http://stackoverflow.com/questions/28213912/python-md5-hashes-of-same-gzipped-file-are-inconsistent
"""

import gzip
import hashlib

f_name = '/etc/passwd'
output_template = '/tmp/test{}.gz'


def digest(filename: str) -> str:
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


block_size = 4096
print("The default way - non identical outputs")
for x in range(0, 3):
    input_handle = open(f_name, 'rb')
    output_filename = output_template.format(x)
    my_zip = gzip.open(output_filename, 'wb')
    try:
        for chunk in iter(lambda: input_handle.read(block_size), b''):
            my_zip.write(chunk)
    finally:
        input_handle.close()
        my_zip.close()
    print(digest(output_filename))

print("The right way to get identical outputs")
for x in range(3, 6):
    input_handle = open(f_name, 'rb')
    output_filename = output_template.format(x)
    my_zip = gzip.GzipFile(
        filename='',  # do not emit filename into the output gzip file
        mode='wb',
        fileobj=open(output_filename, 'wb'),
        mtime=0,  # do not emit modification time information into the output gzip file
    )

    try:
        for chunk in iter(lambda: input_handle.read(block_size), b''):
            my_zip.write(chunk)
    finally:
        input_handle.close()
        my_zip.close()
    print(digest(output_filename))
