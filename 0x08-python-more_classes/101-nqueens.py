#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row on the left side
    for i in range(col):
        if board[i] == row or \
           board[i] == row - col + i or \
           board[i] == row + col - i:
            return False
    return True

def solve_nqueens_util(board, col, n):
    if col == n:
        print_solution(board, n)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[col] = i
            solve_nqueens_util(board, col + 1, n)

def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1 for _ in range(n)]
    solve_nqueens_util(board, 0, n)

def print_solution(board, n):
    solution = [[i, board[i]] for i in range(n)]
    print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
