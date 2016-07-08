#!/usr/bin/python3


class Book(object):
    # constructor

    def __init__(self, price):
        # call parent constructor
        super(Book, self).__init__()
        self.__price = price
    # getters/setters

    def getPrice(self):
        return self.__price

    def setPrice(self, newprice):
        self.__price = newprice
    # printing function

    def printMe(self):
        print('price is', self.__price)
