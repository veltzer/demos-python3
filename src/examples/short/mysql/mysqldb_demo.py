#!/usr/bin/python3

'''
simple example of how to use a mysql database using pythons
MySQLdb module.
Note that this module is not ported to python3 and so this example
is python2 specific.

catching errors is done with:
except MySQLdb.Error, e:
	print('Error {0}: {1}'.format(*e))
	sys.exit(1)
'''

import MySQLdb  # for connect

params = {
    'db': 'myworld',
        'read_default_file': '~/.my.cnf',
}
with MySQLdb.connect(**params) as cursor:
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()[0]
    print('Database version is [{0}]'.format(data))
    cursor.execute('SHOW TABLES')
    for x in cursor:
        print(x[0])
