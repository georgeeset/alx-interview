#!/usr/bin/python3
"""
A function that returns a list of lists of integers representing
the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle
    parameters:
        n [int]:
            the number of rows of Pascal's triangle to recreate
    return:
        [list of lists of ints]:
            representation of Pascal's triangle
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")
    big_list = []
    for i in range(n):
        small_list = []

        for j in range(i + 1):
            if i == 0 or j == 0 or i == j or i == 1:
                small_list.append(1)
            elif i > 1 and i > j:
                small_list.append(big_list[i - 1][j - 1] + big_list[i - 1][j])

        big_list.append(small_list)

    return big_list
