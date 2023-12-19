#!/usr/bin/python3
"""
This module defines a `Square` class that represents
    a square with a given side length and position.

The `Square` class provides methods to calculate the area
    of the square and print it with the character #.
The `size` and `position` attributes can be accessed
    and modified using the getter and setter methods.

If the size of the square is 0, the `my_print` method prints
    an empty line. If the position of the square contains a second
    element greater than 0, the `my_print` method prints
    the corresponding number of empty lines
    before printing the square at the specified location.

If the `position` attribute is not a tuple of 2 positive integers,
    or if the `size` attribute is not a positive integer,
    the class raises a `TypeError` or `ValueError` exception, respectively.

Example usage:
    s = Square(5, (2, 3))
    s.size = 10
    s.position = (1, 1)
    s.area()  # Returns 100
    s.my_print()  # Prints the square at position (1, 1)
        with side length 10 and character #

Author: Abdullah Bedwey
Date created: 27-6-2023
"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The side length of the square.
        position (tuple): The position of the square.

    Methods:
        area(): Returns the area of the square.
        my_print(): Prints the square with the character #.

    Raises:
        TypeError: If the size is not an integer or
        if the position is not a tuple of 2 positive integers.
        ValueError: If the size is less than 0 or
        if the position contains negative integers.

    Examples:
        >>> s = Square(10, (2, 3))
        >>> s.area()
        100
        >>> s.size
        10
        >>> s.size = 5
        >>> s.area()
        25
        >>> s.position
        (2, 3)
        >>> s.position = (1, 1)
        >>> s.my_print()
         #####
         #####
         #####
         #####
         #####
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 or \
                not all(isinstance(i, int) for i in position) or \
                not all(i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
