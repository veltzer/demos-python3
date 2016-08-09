#!/usr/bin/python3

'''
This example explores loading/saving dictionaries in python from/to files

Notes:
- python sets are not JSON serializable
'''

import json  # for dump, load

my_dict = {
    'one': 'onev',
    'two': 'twov',
}
my_set = {
    'one',
    'two',
}

filename = '/tmp/json_store.json'

with open(filename, 'w') as f:
    json.dump(my_dict, f, indent=4)
    #json.dump(my_set, f)

with open(filename) as f:
    other_dict = json.load(f)
    #other_set = json.load(f)
print(other_dict)
#print(other_set)
