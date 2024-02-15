#!/usr/bin/python3

"""Defines the Rectangle class

Classes:
        Rectangle: Defines a rectangle
Example:
        To use this module import the Rectangle class and create an instance
        ```python
        from models.rectangle import Rectangle

        r = Rectangle()
        ```
"""
from models.base import Base


class Rectangle(Base):
    """ Defines a rectangle

    Attributes:
        id (int): A unique identifier to each instance
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x
        y (int): y

    Methods:
        __init__: initalize the new instance of the Rectangle class
        __str__: returns the rectangle in the format
                [Rectangle] (<id>) <x>/<y> - <width>/<height>
        display: outputs the representation of rectangle using the character #

    Properties:
        width (setter and getter): set and get the width of the rectangle
        height (setter and getter): set and get the height of the rectangle

    Example:
    >>> r = Rectangle(3, 2)
    >>> print(r.id)
    1
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # iniatilize id using the base class
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """Verifies width before assigning
        It must be an integr and greater than 0
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 1:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """Verifies height before assigning
        It must be an integer and greater than 0
        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 1:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """Verifies x before assigning
        It must be an integer and greater or equal to 0
        """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """Verifies y before assigning
        It must an integer and greater than or equal to 0
        """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - ' \
            f'{self.width}/{self.height}'

    def area(self):
        """Returns the area of the rectangle instance (l * b)"""
        return self.width * self.height

    def display(self):
        """Displays the rectangle instance with the character #"""
        print('\n' * self.y + "\n".join([(' ' * self.x) + '#' * self.width]
                                        * self.height))

    def update(self, *args, **kwargs):
        """Updates the attribute of the rectangle instance
        if args exits and it not None it update in the order;
            id -> width -> height -> x -> y
        otherwise it uses the kwargs order of keys
        """
        iskey = False
        if not len(args):
            iskey = True
            args = kwargs.values()

        for key, value in zip(kwargs if iskey else self.__dict__, args):
            setattr(self, key, value)
