#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Check that result.max_integer fail when function run
        self.assertAlmostEqual(max_integer([2, 4, 8, 6]), 8)

    def test_only_negative_numbers(self):
        self.assertAlmostEqual(max_integer([-1, -3, -5, -7]), -1)

    def test_negative_and_positive_numbers(self):
        self.assertAlmostEqual(max_integer([10, -40, 90, 50]), 90)

    def test_floats(self):
        self.assertAlmostEqual(max_integer([1.5, 3.4, 2, 0.5]), 3.4)

    def test_empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_one_character(self):
        """test with one character"""
        self.assertRaises(TypeError, max_integer, [2, "g", 8, 6])

if __name__ == '__main__':
    unittest.main()
