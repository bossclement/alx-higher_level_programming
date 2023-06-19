#!/usr/bin/python3
"""Unittest module to test rectangle module."""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Test my rectangle class."""

    def test_id(self):
        r1 = Rectangle(10, 2, 1, 1)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10, 1, 1)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 1, 1, 12)
        self.assertEqual(r3.id, 12)

    def test_width(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None)

        r2 = Rectangle(2, 10, 1, 1)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(10, 2, 1, 1, 12)
        self.assertEqual(r3.width, 10)