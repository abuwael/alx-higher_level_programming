#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    maxNumber = my_list[0]
    for idx in range(length):
        if maxNumber < my_list[idx]:
            maxNumber = my_list[idx]
    return maxNumber
