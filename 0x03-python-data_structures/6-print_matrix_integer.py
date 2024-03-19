#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for i2 in range(len(matrix[i])):
            if i2 != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][i2]), end='')
        print()
