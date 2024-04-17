#!/usr/bin/python3
"""
Author: Abdullah Bedwey
Date: 12/7/2023
"""


import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
