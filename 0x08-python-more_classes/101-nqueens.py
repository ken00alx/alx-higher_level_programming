#!/usr/bin/python3
import sys

def nqueens(n):
    def is_safe(board, row, col):
        # check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # check upper left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # check upper right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve(board, row):
        if row == n:
            # all queens have been placed
            print(board)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, row + 1)
                # backtrack
                board[row][col] = 0

    if not isinstance(n, int) or n < 4:
        print("N must be a number and at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solve(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = int(sys.argv[1])
    nqueens(n)
