#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def test_id_increment_when_none(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)
        Base._Base__nb_objects = 0  # reset __nb_objects to zero for each test

    def test_id_when_not_none(self):
        r = Rectangle(2, 4, id=16)
        self.assertEqual(r.id, 16)
        Base._Base__nb_objects = 0  # reset __nb_objects to zero for each test

    def test_id_with_multiple_instance(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        r3 = Rectangle(5, 6)
        r4 = Rectangle(7, 8, 0, 0, 9)
        self.assertEqual(r4.id, 9)
        Base._Base__nb_objects = 0  # reset __nb_objects to zero for each test
