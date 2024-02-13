#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0  # reset __nb_objects to zero for each test

    def test_id_increment_when_none(self):
        """Test that __nb_objects increment when id is None"""
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)

    def test_id_when_not_none(self):
        """Test that self.id is assigned id when not None"""
        r = Rectangle(2, 4, id=16)
        self.assertEqual(r.id, 16)

    def test_id_with_multiple_instance(self):
        """Test with multiple instances"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        r3 = Rectangle(5, 6)
        r4 = Rectangle(7, 8, 0, 0, 9)
        self.assertEqual(r4.id, 9)

    def test_width_with_types(self):
        """Raises TypeError when width is not an integer"""
        self.assertRaises(TypeError, Rectangle, 2.3, 3)

    def test_height_with_types(self):
        """Raises TypeError when height is not an integer"""
        self.assertRaises(TypeError, Rectangle, 1, 3.3)

    def test_x_with_types(self):
        """Raises TypeError when x is not an integer"""
        self.assertRaises(TypeError, Rectangle, 1, 2, 3.0, 4)

    def test_y_with_types(self):
        """Raises TypeError when y is not an integer"""
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4.1)

    def test_width_with_values(self):
        """Raises valueError when width is 0 or less"""
        self.assertRaises(ValueError, Rectangle, 0, 3)

    def test_height_with_values(self):
        """Raises valueError when height is 0 or less"""
        self.assertRaises(ValueError, Rectangle, 3, 0)

    def test_x_with_values(self):
        """Raises ValueError when x is less than 0"""
        self.assertRaises(ValueError, Rectangle, 1, 2, -1, 4)

    def test_y_with_values(self):
        """Raises ValueError when y is less than 0"""
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -1)

    def test_area(self):
        """Test that the area method correctly returns the area of the
        rectangle (l * b)
        """
        r = Rectangle(4, 10)
        self.assertEqual(r.area(), 40)

    def test_display(self):
        """Test the Display method"""
        r = Rectangle(3, 2)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            printed_output = mock_stdout.getvalue()

        expected_output = "###\n" \
                          "###\n"
        self.assertEqual(printed_output, expected_output)
