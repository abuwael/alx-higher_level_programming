#!/usr/bin/python3
"""
Author: Abdullah Bedwey
Date: 12/7/2023
"""


import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
