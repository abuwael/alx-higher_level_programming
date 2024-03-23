#!/usr/bin/python3
def number_keys(a_dictionary):
    ctr = 0
    keys = list(a_dictionary.keys())
    for i in a_dictionary:
        ctr += 1
    return ctr
