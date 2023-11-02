#!/user/bin/python3
"""
N-Queens solution
"""
from typing import List


def solve_nqueens(n: int) -> List[list[str]]:
    """
    solve the nxn  chessboard with n queens on board
    """
    col = set()
    # positive diagonal of board = (row + C)
    pos_diagonal = set()

    # negative diagnoal negdiagonal
    neg_diagonal = set()

    # results will be stored here
    result_list = []

    # board setup. n by n empty at first with '.'
    board = [['.'] * n for i in range(n)]

    # queen position [row, column]
    queen_position = []

    def backtrack(board_row):
        if board_row == n:
            board_copy = ["".join(row) for row in board]
            result_list.append(queen_position)
            return
    
        for c in range(n):
            if c in col or (board_row + c) in pos_diagonal or (board_row -c) in neg_diagonal:
                continue

            col.add(c)
            pos_diagonal.add(board_row + c)
            neg_diagonal.add(board_row - c)
            queen_position = board[board_row][c]

            backtrack(board_row + 1)

            col.remove(c)
            pos_diagonal.remove(board_row + c)
            neg_diagonal.remove(board_row - c)
            board[board_row][c] = '.'

    backtrack(0)
    return result_list

print(solve_nqueens(4))
