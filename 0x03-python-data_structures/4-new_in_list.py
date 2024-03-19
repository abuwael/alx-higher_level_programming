#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    new_list = my_list[:]

    if idx >= 0 and idx <= length:
        new_list[idx] = element

    return (new_list)
