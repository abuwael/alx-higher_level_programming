#!/usr/bin/python3

"""
Author: Bedwey
Date: 11/7/2023
"""


def append_write(filename="", text=""):
    """
    append a string to a text file (UTF8)
        and returns the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
