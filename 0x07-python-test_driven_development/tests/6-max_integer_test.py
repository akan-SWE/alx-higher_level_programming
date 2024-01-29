#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_integer([229, 52182, 22, 332]), 52182)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-9, -100, -1, -28]), -1)

    def test_empty_list(self):
        self.assertEqual(max_integer(), None)

    def test_duplicate_numbers(self):
        self.assertEqual(max([2, 8, 7, 8, 1]), 8)

    def test_single_number(self):
        self.assertEqual(max([82]), 82)

    def test_large_numbers(self):
        self.assertEqual(max([111000000000, 999888, 1010101001010000]),
                         1010101001010000)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-3, 7, 1, -10, 5]), 7)

    def test_two_numbers(self):
        self.assertEqual(max_integer([5, 9]), 9)
