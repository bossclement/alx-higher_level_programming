#!/usr/bin/python3
"""Unittest module to test rectangle module."""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Test my rectangle class."""

    def test_width(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None)

        r2 = Rectangle(2, 10, 1, 1)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(10, 2, 1, 1, 12)
        self.assertEqual(r3.width, 10)

    def test_height(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None)

        r2 = Rectangle(2, 10, 1, 1)
        self.assertEqual(r2.height, 10)

        r3 = Rectangle(10, 2, 1, 1, 12)
        self.assertEqual(r3.height, 2)