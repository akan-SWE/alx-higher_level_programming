#!/usr/bin/python3


"""This module contains the Square class"""


class Square:
    """Defines a square class

    Attribute:
        size: size of the square
    Methods:
        __init__: initialize size and also verify the data
        area: returns the area of a square
        my_print: Outputs a square based on the size and position
    Property:
        size (getter): Get the current size of the square
        size (setter): Set the current size of the square
        position (getter): returns the position
        position (setter): sets the position

    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size  # call the (setter) size
        self.position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size != 0:
            if self.position[1] > 0:
                for _ in range(self.position[1]):
                    print()

            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)
        else:
            print()

    @property
    def position(self):
        return self.__position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or len(value) != 2:
            # position must be a tuple and length of 2
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
            # all data in tuple must be a positive integer
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            # all check pass
            self.__position = value
