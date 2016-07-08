#!/usr/bin/python3

'''
This is a fairly simple basic OO example
'''


class Book(object):
    NumberOfBooks = 17
    ''' constructor '''

    def __init__(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def setPrice(self, newprice):
        self.__price = newprice

    def printMe(self):
        print('price is', self.__price)

''' Lets show how we use our object... '''
b = Book(50)
b.printMe()
b.setPrice(60)
b.printMe()
