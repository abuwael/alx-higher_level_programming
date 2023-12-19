#!/usr/bin/python3
"""Example of Square class.
"""


class Square:
    """Square Class.
    Args:
        size (int): Description of `size`.
    Attributes:
        size (int): Description of `size`.
    Methods:
        area():
            returns the current square area.
    """
    def __init__(self, size=0):
        """Initializes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area."""
        return (self.__size * self.__size)
