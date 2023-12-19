#!/usr/bin/python3
"""Example of Square class.
"""


class Square:
    """Square Class.
    Attributes:
        size (int): Description of `size`.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
