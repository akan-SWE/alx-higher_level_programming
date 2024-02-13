#!/usr/bin/python3
"""Module providing the Base class for the project

This module defines the Base class, which serves as the foundation for other
classes in the project

Classes:
        Base: The base class providing common functionality
Example:
        To use this module import the Base class and create an instance
        ```python
        from models.base import Base

        base = Base()
        ```
"""


class Base:
    """ The base class providing common functionality

    Attributes:
        id (int): A unique identifier to each instance
        __nb_objects (int): counts the number of times Base is called
    when id is None

    Methods:
        __init__: initalize the new instance of the Base class

    Example:
    >>> base = Base()
    >>> print(base.id)
    1
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:  # id not None
            self.id = id
        else:  # id is None
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
