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
        r = Rectangle(3, 2, 2, 2)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            printed_output = mock_stdout.getvalue()

        expected_output = "\n\n  ###\n" \
                          "  ###\n"
        self.assertEqual(printed_output, expected_output)

    def test_str(self):
        """Test the __str__ method"""
        r = Rectangle(3, 2, 1, 1)
        self.assertEqual('[Rectangle] (1) 1/1 - 3/2', r.__str__())

    def test_update_without_keys(self):
        """Test that the update method correctly updates values
        of attributes when pased as no-keyword argument"""
        r = Rectangle(1, 2, 22, 33, 8)
        r.update(22, 32, 10, 11, 10)
        self.assertEqual(r.id, 22)
        self.assertEqual(r.width, 32)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 11)
        self.assertEqual(r.y, 10)

    def test_update_with_keys(self):
        """Test that the update method correctly updates
        values of attributes when passed as key-worded argument
        """
        r = Rectangle(1, 2, 22, 33, 8)
        r.update(width=22, height=32, x=10, y=11, id=10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 22)
        self.assertEqual(r.height, 32)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 11)
