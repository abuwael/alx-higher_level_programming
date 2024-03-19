#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    index = 0
    new_string = my_string[:]

    for char in range(length):
        if (my_string[char] == 'c' or my_string[char] == 'C'):
            new_string = new_string[:(char - index)] + my_string[(char + 1):]
            index += 1

    return (new_string)
