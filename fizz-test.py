#!/usr/bin/env python

# FizzBuzz unit test

import unittest
from fizz import isBuzz,isFizz


class TestStringMethods(unittest.TestCase):
    # Test 1 should pass
    def test_fizz1(self):
        self.assertTrue(isFizz(3))
    def test_fizz2(self):
        self.assertFalse(isFizz(2))

    def test_buzz1(self):
        self.assertTrue(isBuzz(5))
    def test_buzz2(self):
        self.assertTrue(isBuzz(25))
    def test_buzz3(self):
        self.assertFalse(isBuzz(2))
    def test_buzz4(self):
        self.assertFalse(isBuzz(101))

    def test_fizzbuzz1(self):
        self.assertTrue(isFizz(15) and isBuzz(15))
    def test_fizzbuzz2(self):
        self.assertTrue(isFizz(30) and isBuzz(30))
    def test_fizzBuzz3(self):
        self.assertFalse(isFizz(31) and isBuzz(31))

if __name__ == '__main__':
    unittest.main()
