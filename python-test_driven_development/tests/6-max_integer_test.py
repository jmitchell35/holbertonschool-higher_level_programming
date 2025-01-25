#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):  # Regular input
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([0, -1, -2, -3, -4]), 0)

    def test_value_max_integer(self):  # list of wrong values
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(["string", 's', '\n']), 'string')
        self.assertEqual(max_integer([-0.0, 0.0]), -0.0)
        self.assertEqual(max_integer(
            [float('-inf'), float('inf')]), float('inf'))
        self.assertEqual(max_integer([0.0, float('nan')]), 0.0)
        self.assertEqual(max_integer(
            [[], [1, 2, 3], [4, 5, 6, 7]]), [4, 5, 6, 7])
        self.assertRaises(
                TypeError, max_integer, [{}, {1, 2, 3}, {4, 5, 6, 7}])
        self.assertRaises(
                TypeError, max_integer, [{"key": 1}, {"key2": "value2"}])

    def test_type_max_integer(self):  # wrong type input
        self.assertEqual(max_integer("string"), 't')
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer(" "), ' ')
        self.assertEqual(max_integer("$%"), '%')
        self.assertEqual(max_integer("$% \n rafgretrwegrwe !@ 678"), 'w')
        self.assertRaises(
                TypeError, max_integer, **{"key1": 1, "key2": 2})
        self.assertRaises(TypeError, max_integer, {1, 2})
        self.assertRaises(TypeError, max_integer, float(1))
        self.assertRaises(TypeError, max_integer, 1)

    def test_edgecases_max_integers(self):  # others / edge cases
        self.assertEqual(max_integer(), None)
