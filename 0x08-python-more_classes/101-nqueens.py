#!/usr/bin/python3
import sys


def nqueens(N):
    """
    Solves the N queens problem and prints every
        possible solution to the problem.
    One solution per line, in the format
        [[row1, col1], [row2, col2], ..., [rowN, colN]]

    Args:
    - N (str or int): The number of queens to place on an NxN chessboard.

    Raises:
    - ValueError: If N is not a valid integer.
    - ValueError: If N is less than 4.

    Returns:
    - None
    """

    def is_safe(board, row, col):
        """
        Returns True if it is safe to place a queen
            at the given position on the board.

        Args:
        - board (list of lists): The current state of the chessboard.
        - row (int): The row to check.
        - col (int): The column to check.

        Returns:
        - bool: True if it is safe to place a queen
            at the given position, False otherwise.
        """
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col, solutions):
        """
        Recursively solves the N queens problem for the given board and column.

        Args:
        - board (list of lists): The current state of the chessboard.
        - col (int): The current column to place a queen in.
        - solutions (list): A list of solutions to the N queens problem.

        Returns:
        - None
        """
        if col == N:
            solution = []
            for row in range(N):
                col_index = [i for i in range(N) if board[row][i] == 1][0]
                solution.append([row, col_index])
            solutions.append(solution)
            return
        for row in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, col+1, solutions)
                board[row][col] = 0

    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve(board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
