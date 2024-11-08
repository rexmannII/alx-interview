N-Queens Solver
This Python program solves the N-Queens problem using the backtracking algorithm, placing N non-attacking queens on an N×N chessboard.

Requirements
Python 3.x
Command-line arguments for N (the size of the chessboard)
Usage
Run the program with the desired size of the chessboard:

bash
Copy code
./nqueens.py N
Where N is an integer greater than or equal to 4.

Example:
bash
Copy code
./nqueens.py 4
Output:
css
Copy code
. Q . .
. . . Q
Q . . .
. . Q .
Input Validation
If N is not provided, it will print:
Usage: nqueens N

If N is not an integer, it will print:
N must be a number

If N is less than 4, it will print:
N must be at least 4

Algorithm
The program uses backtracking to place queens on the board, ensuring no two queens threaten each other. The solution is printed as a grid with Q for queens and . for empty spaces.

License
MIT License
