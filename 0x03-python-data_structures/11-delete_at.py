#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if length != 0 and idx >= 0 and length > idx:
        del my_list[idx]
    return my_list
