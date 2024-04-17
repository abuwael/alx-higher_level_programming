#!/usr/bin/python3
"""
Author: Abdullah Bedwey
Date: 12/7/2023
"""


def class_to_json(obj):
    """
        Return the dictionary represntation of a simple data structure
    """
    return obj.__dict__
