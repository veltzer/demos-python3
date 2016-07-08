#!/usr/bin/python3

login = raw_input('insert login: ')
full_name = raw_input('insert full name: ')
password = raw_input('insert password: ')

if login == '':
    print('Error: Login must not be empty')
else:
    print('login: ', login)
    print('full name: ', full_name)
    print('password: ', password)
