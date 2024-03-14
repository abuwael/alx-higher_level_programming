#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        isLower = (ord(str[i]) >= 97 and ord(str[i]) <= 122)
        print(chr(ord(str[i]) - 32) if isLower else str[i], end="")
    print("{}".format(""))
