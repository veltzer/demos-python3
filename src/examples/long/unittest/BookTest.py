#!/usr/bin/python3

import unittest  # for main
import Book  # for Book


class BookTest(unittest.TestCase):
    # tests

    def setUp(self):
        print('in setUp')

    def tearDown(self):
        print('in tearDown')

    def testBasic(self):
        print('in testBasic')
        p = Book.Book(50)
        self.assertTrue(50 == p.getPrice())

    def testMore(self):
        print('in testMore')
        p = Book.Book(50)
        p._Book__price = 60
        self.assertTrue(60 == p.getPrice())

    def runTest(self):
        print('in runTest')
        p = Book.Book(50)
        p._Book__price = 60
        self.assertTrue(60 == p.getPrice())

unittest.main()
