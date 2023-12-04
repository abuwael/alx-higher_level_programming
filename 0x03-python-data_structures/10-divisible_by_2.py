#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tup = []
    i = 0
    while i < len(my_list):
        tup.append((my_list[i] % 2) == 0)
        i += 1
    return tuple(tup)
