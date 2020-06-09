#!/usr/bin/python3
""" Unittests for base """

import unittest
from models import base
from models.base import Base

class TestBase(unittest.TestCase):
    """ Test cases for Base class """

    def test_none(self):
        a = Base()
        self.assertEqual(a.id, 1)

    def test_neg(self):
        b = Base(-2)
        self.assertEqual(b.id, -2)

    def test_pos(self):
        c = Base(2)
        self.assertEqual(c.id, 2)

    def test_none(self):
        d = Base(None)
        self.assertEqual(d.id, 1)
