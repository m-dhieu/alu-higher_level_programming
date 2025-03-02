#!/usr/bin/python3


"""This module solves the N queens problem."""


import sys


def is_safe(board, row, col, n):
    """Checks if a queen can be placed on board[row][col]."""

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    """A recursive utility function to solve N Queens problem."""

    # If all queens are placed then return true
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    # Consider column and try placing queen in all rows
    res = False
    for i in range(n):

        if is_safe(board, i, col, n):

            # Place queen in board
            board[i][col] = 1

            # Make result true if any placement is possible
            res = solve_nqueens_util(board, col + 1, n, solutions) or res

            # If placing queen in board doesn't lead to a solution,
            # remove queen from board
            board[i][col] = 0  # BACKTRACK

    # If queen can't be placed in any row in this column, return false
    return res


def solve_nqueens(n):
    """Solve the N queens problem."""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    if not solve_nqueens_util(board, 0, n, solutions):
        return []  # No solutions found

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)

    for solution in solutions:
        print(solution)
