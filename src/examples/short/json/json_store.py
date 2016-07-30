#!/usr/bin/python3

'''
This example explores loading/saving dictionaries in python from/to files
'''

import json  # for dump, load

my_dict = {
    'one': 'onev',
    'two': 'twov',
}

filename = '/tmp/json_store.json'

with open(filename, 'w') as f:
    json.dump(my_dict, f, indent=4)

with open(filename) as f:
    other_dict = json.load(f)
print(other_dict)
