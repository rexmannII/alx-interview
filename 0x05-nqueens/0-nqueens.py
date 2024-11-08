#!/usr/bin/python3

import sys

def print_solution(board):
    """ Prints the chessboard for one solution """
    for row in board:
        print("".join("Q" if col == 1 else "." for col in row))

def is_safe(board, row, col, N):
    """ Checks if it's safe to place a queen at position (row, col) """
    # Check column for conflicts
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal for conflicts
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal for conflicts
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, row, N):
    """ Solves the N-Queens problem using backtracking """
    if row == N:
        # If all queens are placed, print the solution
        print_solution(board)
        return True
    
    solution_found = False
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place the queen
            solution_found = solve_nqueens(board, row + 1, N) or solution_found
            board[row][col] = 0  # Backtrack

    return solution_found

def nqueens(N):
    """ Solves the N-Queens problem for an N x N board """
    board = [[0 for _ in range(N)] for _ in range(N)]  # Initialize an empty board
    if not solve_nqueens(board, 0, N):
        print("Solution does not exist")

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Try to convert input to integer and check if it's >= 4
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Call the function to solve the problem
    nqueens(N)
