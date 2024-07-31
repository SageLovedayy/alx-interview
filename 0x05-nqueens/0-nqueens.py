#!/usr/bin/python3

import sys


def is_valid(board, row, col):
    """Checks if there's a queen in the same column
    or diagonal"""
    for i in range(row):
        if board[i] == col:
            return False
        # Check for queens in the diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    if row == N:
        solutions.append(board[:])
        return
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)


def print_solutions(solutions):
    for solution in solutions:
        result = []
        for row, col in enumerate(solution):
            result.append([row, col])
        print(result)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
