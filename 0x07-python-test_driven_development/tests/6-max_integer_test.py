#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ class for MaxInteger testing """
    def test_end(self):
        tlist = [1, 2, 3]
        self.assertEqual(max_integer(tlist), 3)

    def test_start(self):
        tlist = [3, 2, 1]
        self.assertEqual(max_integer(tlist), 3)

    def test_middle(self):
        tlist = [2, 3, 1]
        self.assertEqual(max_integer(tlist), 3)

    def test_negative(self):
        tlist = [-3, 2, 1]
        self.assertEqual(max_integer(tlist), 2)

    def test_negative_all(self):
        tlist = [-3, -2, -1]
        self.assertEqual(max_integer(tlist), -1)

    def test_one(self):
        tlist = [1]
        self.assertEqual(max_integer(tlist), 1)

    def test_none(self):
        tlist = []
        self.assertEqual(max_integer(tlist), None)
