import sys

def is_safe(board, row, col):
    # Check if it is safe to place a queen at board[row][col]
    
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check for queens in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    # Check for queens in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    return True

def solve_nqueens(N):
    # Initialize an empty NxN chessboard
    board = [['.' for _ in range(N)] for _ in range(N)]
    
    def backtrack(row):
        # Base case: All queens have been placed
        if row == N:
            # Print the solution
            for i in range(N):
                print(''.join(board[i]))
            print()
            return
        
        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col):
                # Place the queen at board[row][col]
                board[row][col] = 'Q'
                
                # Recur to place queens in the next row
                backtrack(row + 1)
                
                # Backtrack: Remove the queen from board[row][col]
                board[row][col] = '.'
    
    backtrack(0)

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