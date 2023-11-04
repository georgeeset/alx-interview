#!/usr/bin/python3
"""Solving N Queens Problem using backtracking"""
import sys
from typing import List


def printSolution(board: List[List], n: int) -> None:
    """Print allocated positions to the queen"""
    positions = []

    for row in range(n):
        for column in range(n):
            if column == board[row]:
                positions.append([row, column])
    print(positions)


def is_safe(board: List[List], r: int, c: int, row: int) -> bool:
    """Checks if the position is safe"""
    return board[r] in (c, c - r + row, r - row + c)


def recursive_fill(board: List, row, n) -> None:
    """recursively select locations"""
    if row == n:
        printSolution(board, n)

    else:
        for c in range(n):
            allowed = True
            for r in range(row):
                if is_safe(board, r, c, row):
                    allowed = False
            if allowed:
                board[row] = c
                recursive_fill(board, row + 1, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])

    board = [0 * n for i in range(n)]
    recursive_fill(board, 0, n)
