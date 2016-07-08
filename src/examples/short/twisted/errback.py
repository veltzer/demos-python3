#!/usr/bin/python3

'''
An example of using errbacks in twisted.
'''

# from twisted.internet.protocol import Factory,Protocol
from twisted.internet import reactor
from twisted.web.client import getPage
# from twisted.protocols.basic import LineReceiver


def my_other_callback(content):
    print('in other_callback', content)
    reactor.stop()


def my_callback(content):
    print('in callback', content)
    defr = getPage('http://localhost/~user/')
    defr.addCallback(my_other_callback)
    # raise Exception('this is an exception')
    # reactor.stop()


def my_errback(error):
    print('in error', error)
    reactor.stop()

defr = getPage('http://localhost')
defr.addCallback(my_callback)
defr.addErrback(my_errback)
reactor.run()
