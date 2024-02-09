#!/usr/bin/python3

"""Student module"""


class Student:
    """Defines a student

    Attribute:
        first_name: the first name of the student
        last_name: the last name of the student
        age: the age of the student
    Methods:
        __init__: initialize the first name, last name and age of the student
        to_json: return a dictionary representation of the student object
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs or attrs == []:
            return {a: self.__dict__[a] for a in attrs if a in self.__dict__}
        return self.__dict__
