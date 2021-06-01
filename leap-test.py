#!/usr/bin/env python

import unittest
from leap import isLeapYr

# Leap year program unit tests.

class TestStringMethods(unittest.TestCase):
    def test_leap1(self):
        self.assertTrue(isLeapYr(2004))
    def test_leap1(self):
        self.assertTrue(isLeapYr(2008))
    def test_leap1(self):
        self.assertFalse(isLeapYr(2000))
    def test_leap1(self):
        self.assertFalse(isLeapYr(2002))
    

if __name__ == '__main__':
    unittest.main()

