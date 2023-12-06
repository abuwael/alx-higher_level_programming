#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for j, val in a_dictionary.items():
        new_dict[j] = val * 2
    return new_dict
