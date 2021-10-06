#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        result = 8
        self.assertEqual(result.max_integer(), [2, 4, 8, 6])
        # Check that result.max_integer fail when function run
        with self.assertRaises(TypeError):
            result.max_integer(2)


if __name__ == '__main__':
    unittest.main()