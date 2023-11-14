#!/usr/bin/python3
"""Given an n x n 2D matrix,
rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix: list) -> None:
    """Rotates a 2D matrix clockwise.
    """
    if type(matrix) != list:
        return
    rows = len(matrix)
    col = len(matrix[0])
    # check if row and column is same length
    if not all(map(lambda x: len(x) == col, matrix)):
        return
    c, r = 0, rows - 1
    for i in range(col * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == col - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
