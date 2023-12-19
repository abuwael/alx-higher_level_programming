#!/usr/bin/python3
"""
This module contains the Square class,
which represents a square with a given side length.
The Square class provides a method to calculate the area of the square,
and the `size` attribute can be accessed
and modified using the getter and setter methods.

Example:
    To create a square with a side length of 5:
    >>> s = Square(5)
    >>> s.area()
    25

    To change the side length of the square:
    >>> s.size = 10
    >>> s.area()
    100

Exceptions:
    The Square class raises a TypeError if the size is not
    an integer and a ValueError if the size is less than 0.

"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The side length of the square.

    Methods:
        area(): Returns the area of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.

    Examples:
        To create a square with a side length of 5:
        >>> s = Square(5)
        >>> s.area()
        25
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)

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
