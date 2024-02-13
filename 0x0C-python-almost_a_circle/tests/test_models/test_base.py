#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_increment_when_none(self):
        b = Base()
        self.assertEqual(b.id, 1)
        Base._Base__nb_objects = 0  # reset __nb_objects to zero for each test

    def test_id_when_not_none(self):
        b = Base(32)
        self.assertEqual(b.id, 32)
        Base._Base__nb_objects = 0  # reset __nb_objects to zero for each test

    def test_id_with_multiple_instance(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(32)
        b4 = Base(42)
        b5 = Base()
        self.assertEqual(b5.id, 3)
        Base._Base__nb_objects = 0  # reset __nb_objects to zero for each test
