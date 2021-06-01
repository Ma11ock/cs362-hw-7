#!/usr/bin/env python

# FizzBuzz unit test

import unittest
from fizz import isBuzz,isFizz


class TestStringMethods(unittest.TestCase):
    # Test 1 should pass
    def test_fizz1(self):
        self.assertTrue(isFizz(3))
    def test_fizz2(self):
        self.assertFalse(2)


if __name__ == '__main__':
    unittest.main()
