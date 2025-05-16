#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_values(self):
        self.assertAlmostEqual(max_integer([2,3,5]), 5)
        self.assertAlmostEqual(max_integer([1,3,2]), 3)
        self.assertAlmostEqual(max_integer([9,3,2]), 9)
        self.assertAlmostEqual(max_integer([1,-3,2]), 2)
        self.assertAlmostEqual(max_integer([-1,-3,-2]), -1)
        self.assertAlmostEqual(max_integer([2]), 2)
        self.assertAlmostEqual(max_integer([]), None)


