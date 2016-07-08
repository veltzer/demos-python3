#!/usr/bin/python3

'''
An example exploring the many ways,right and wrong,to iterate
a dictionary in python.
'''

h = {}
h['keyone'] = 'valone'
h['keytwo'] = 'valtwo'

# this is the most efficient method
# most common and very efficient way (does not guarantee order)...
for (k, v) in h.items():
    print('key is', k)
    print('val is', v)
# each time you get BOTH a key AND value as a tuple so you can use it as a
# tuple...
for x in h.items():
    print(x)
    print('key is', x[0])
    print('val is', x[1])
# this is the same but you only get a key each time
for x in h:
    print(x)
    print('key is', x)
    print('val is', h[x])
# this is less efficient (at least in some versions of python)
for x in h.keys():
    print(x)
    print('key is', x)
    print('val is', h[x])
# this is TERRIBLE performance wise although to a novice it looks
# almost the same... Some versions of python may be smart enough to optimize
# this away but you really shouldn't count on it.
list = h.keys()
for x in list:
    print(x)
    print('key is', x)
    print('val is', h[x])
