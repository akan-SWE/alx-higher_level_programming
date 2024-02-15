#!/usr/bin/env python3

from tests.test_models.test_rectangle import TestRectangle

from models.square import Square
import unittest
from models.base import Base
from unittest.mock import patch
from io import StringIO


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0  # reset __nb_objects to zero for each test

    def test_id_increment_when_none(self):
        """Test that __nb_objects increment when id is None"""
        s = Square(1)
        self.assertEqual(s.id, 1)

    def test_id_when_not_none(self):
        """Test that self.id is assigned id when not None"""
        s = Square(2, id=16)
        self.assertEqual(s.id, 16)

    def test_id_with_multiple_instance(self):
        """Test with multiple instances"""
        s1 = Square(1)
        s2 = Square(3)
        s3 = Square(5)
        s4 = Square(7, 1, 2, 9)
        self.assertEqual(s4.id, 9)

    def test_size_with_types(self):
        """Raises TypeError when width is not an integer"""
        self.assertRaises(TypeError, Square, 2.3)

    def test_x_with_types(self):
        """Raises TypeError when x is not an integer"""
        self.assertRaises(TypeError, Square, 1, 3.0, 4)

    def test_y_with_types(self):
        """Raises TypeError when y is not an integer"""
        self.assertRaises(TypeError, Square, 1, 3, 4.1)

    def test_size_with_values(self):
        """Raises valueError when width is 0 or less"""
        self.assertRaises(ValueError, Square, 0)

    def test_x_with_values(self):
        """Raises ValueError when x is less than 0"""
        self.assertRaises(ValueError, Square, 1, -1, 4)

    def test_y_with_values(self):
        """Raises ValueError when y is less than 0"""
        self.assertRaises(ValueError, Square, 1, 3, -1)

    def test_area(self):
        """Test that the area method correctly returns the area of the
        """
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_display(self):
        """Test the Display method"""
        s = Square(2, 1, 2, 2)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s.display()
            printed_output = mock_stdout.getvalue()

        expected_output = "\n\n ##\n" \
                          " ##\n"
        self.assertEqual(printed_output, expected_output)

    def test_str(self):
        """Test the __str__ method"""
        s = Square(3, 2, 1, 5)
        self.assertEqual('[Square] (5) 2/1 - 3', s.__str__())

    def test_update_without_keys(self):
        """Test that the update method correctly updates values
        of attributes when pased as no-keyword argument"""
        s = Square(1)
        s.update(22, 32, 10, 11, 10)
        self.assertEqual(s.id, 22)
        self.assertEqual(s.width, 32)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 11)
        self.assertEqual(s.y, 10)

    def test_update_with_keys(self):
        """Test that the update method correctly updates
        values of attributes when passed as key-worded argument
        """
        s = Square(1)
        s.update(width=22, height=32, x=10, y=11, id=10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.width, 22)
        self.assertEqual(s.height, 32)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 11)
