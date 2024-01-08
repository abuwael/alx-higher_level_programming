#!/usr/bin/python3
"""
The Rectangle module defines a Rectangle class that represents
    a rectangle and provides methods to set
    and get the width and height of the rectangle.

Author: Abdullah Bedwey
Date created: 3-7-2023
"""


class Rectangle:
    """
    A class representing a rectangle.

    :param width: An integer representing the width of the rectangle.
    :param height: An integer representing the height of the rectangle.

    :raises TypeError: If width or height is not an integer.
    :raises ValueError: If width or height is less than 0.

    :return: A Rectangle object.
    """

    def __init__(self, width=0, height=0):
        """
            Initializes a new Rectangle object.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
            Gets the width of the rectangle.
            :return: An integer representing the width of the rectangle.
            """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
            Sets the width of the rectangle.
            :param value: An integer representing the width of the rectangle.

            :raises TypeError: If value is not an integer.
            :raises ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Gets the height of the rectangle.
            :return: An integer representing the height of the rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
            Sets the height of the rectangle.

            :param value: An integer representing the height of the rectangle.

            :raises TypeError: If value is not an integer.
            :raises ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
