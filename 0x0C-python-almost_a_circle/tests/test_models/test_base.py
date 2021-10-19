#!/usr/bin/python3
"""Unittest for Base, rectangle and square
"""
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):

    def test_none_id(self):
        Base._Base__nb_objects = 0
        f = Base()
        f2 = Base()
        f3 = Base()
        self.assertAlmostEqual(f.id, 1)
        self.assertAlmostEqual(f2.id, 2)
        self.assertAlmostEqual(f3.id, 3)

    def test_instance_(self):
        # Check the instance
        b = Base(56)
        self.assertIsInstance(b, Base)

    def test_id_equal(self):
        c = Base(5)
        self.assertAlmostEqual(c.id, 5)

    def test_no_object(self):
        a = Base("g")
        self.assertIsInstance(a, Base)
         
    def test_id_int(self):
        g = Base()
        self.assertEqual(type(g.id), type(3))

    def test_id_different(self):
        d = Base()
        e = Base()
        self.assertNotEqual(d.id, e.id)

    def test_id_equal(self):
        d = Base(4)
        e = Base(4)
        self.assertEqual(d.id, e.id)

if __name__ == '__main__':
    unittest.main()
