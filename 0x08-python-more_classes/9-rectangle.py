#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Defines a Rectangle class

    Attributes:
        class attributes:
                print_symbol (any type): the symbol to print when
                str method is called
                number_of_instances (int): number of Rectangle instances

        height (int): height of the Rectangle
        width (int): width of the Rectangle

    Properties:
        height (setter and getter): set and get the height of the Rectangle
        width (setter and getter): set and get the width of the Rectangle

    Methods:
        area: area of the Rectangle (h * w)
        perimeter: perimeter of the Rectangle 2(h + w)
        __str__: return the rectangle with the character '#'
        __repr__: return a string representation of a Rectangle instance
        __del__: prints 'Bye rectangle...' before deleting a Rectangle instance
        bigger_or_equal (static): return a rectangle that is bigger or equal
        based on their area
        square (class): returns a Rectangle instance with width and height
        equal to size
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __repr__(self):
        """Returns a string representation of the rectangle for eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.is_invalid_dimension():
            return ""
        return "\n".join([str(self.print_symbol) * self.width] *
                         self.height)

    def area(self):
        return self.height * self.width

    def perimeter(self):
        # if width or height is equal to 0, perimeter is equal to 0
        return 0 if self.is_invalid_dimension() \
            else 2 * (self.height + self.width)

    def is_invalid_dimension(self):
        return not self.height or not self.width

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size."""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
