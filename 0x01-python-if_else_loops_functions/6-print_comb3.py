#!/usr/bin/python3
for first in range(0, 10):
    for second in range(0, 10):
        if first != second and first < second:
            if first + second != 17:
                print("{}{}".format(first, second), end=", ")
            else:
                print("{}{}".format(first, second))
