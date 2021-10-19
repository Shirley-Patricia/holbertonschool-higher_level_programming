#!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest

from models.rectangle import Rectangle
from models.base import Base

class Test_Rectangle(unittest.TestCase):

    def setUp(self):
        #r1 = Rectangle(10, 2)
        pass

    def test_instance_(self):
        # Check the instance
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Base)
    
    def test_validation_inst_str(self):
        self.assertRaises(TypeError, Rectangle, (2, "g", 8, 6))
    
    def test_validation_inst_str2(self):
        self.assertRaises(TypeError, Rectangle, (2, 5, "8", 6))

    def test_valid_inst_str_short(self):
        self.assertRaises(TypeError, Rectangle, (2, "15"))

    def test_valid_inst_value(self):
        self.assertRaises(ValueError, Rectangle, (2, 10, 8, -1))

    def test_valid_inst_value2(self):
        self.assertRaises(ValueError, Rectangle, (2, -10, 8, 1))

    def tearDown(self):
        pass