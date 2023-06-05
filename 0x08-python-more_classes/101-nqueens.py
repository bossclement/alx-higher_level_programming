import sys

"""Docs for my module"""


def is_safe(board, row, col):
    # Check if it is safe to place a queen at board[row][col]

    # Check for queens in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check for queens in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check for queens in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(N):
    # Initialize an empty board
    board = [-1] * N
    solutions = []

    def backtrack(row):
        # Base case: All queens have been placed
        if row == N:
            solutions.append(list(enumerate(board)))
            return

        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col):
                # Place the queen at board[row]
                board[row] = col

                # Recur to place queens in the next row
                backtrack(row + 1)

    backtrack(0)

    # Print the solutions
    for solution in solutions:
        print(solution)
    print()


if __name__ == '__main__':
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Parse the input N
        N = int(sys.argv[1])

        # Check the value of N
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        # Solve the N Queens problem
        solve_nqueens(N)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
