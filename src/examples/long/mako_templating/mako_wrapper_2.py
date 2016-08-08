#!/usr/bin/python3

import sys  # for argv, stderr, exit
import mako.template  # for Template
import mako.lookup  # for TemplateLookup
import os  # for os.chmod
import datetime  # for datetime

#
# functions #
#


def years(x):
    curr_year = datetime.datetime.now().year
    return ','.join(map(str, range(x, curr_year + 1)))

#
# code #
#
if len(sys.argv) != 3:
    print(sys.argv[0] + ': usage: ' + sys.argv[
          0] + ' [input] [output]', file=sys.stderr)
    sys.exit(1)

input_encoding = 'utf-8'
output_encoding = 'utf-8'
p_input = sys.argv[1]
p_output = sys.argv[2]

mylookup = mako.lookup.TemplateLookup(
    directories=['.'], input_encoding=input_encoding, output_encoding=output_encoding)
template = mako.template.Template(
    filename=p_input, lookup=mylookup, output_encoding=output_encoding, input_encoding=input_encoding)
file = open(p_output, 'w')
file.write(template.render(foo='bar', years=years))
file.close()
os.chmod(p_output, 0o444)
