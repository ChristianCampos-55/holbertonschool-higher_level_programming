#!/usr/bin/python3
""" Module that hosts all tests for the Rectangle Class """
import unittest
from models import rectangle
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Unit tests for rectangle """

    def test_rect_id(self):
        a = Rectangle(5, 2)
        b = Rectangle(3, 1)
        c = Rectangle(4, 2, 0, 0, 8)
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, 8)
