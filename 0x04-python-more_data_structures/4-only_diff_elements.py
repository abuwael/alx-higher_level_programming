#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uniq_to_set = (set_1 ^ set_2)
    return uniq_to_set
