#!/usr/bin/python3

"""
Author: Abdullah Bedwey
Date 11/7/2023
"""


def read_file(filename=""):
    """
        read file and print it out
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
