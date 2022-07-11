# The N Queen is the problem of placing N chess queens on an N×N chessboard
# so that no two queens attack each other

# The expected output is a binary matrix which has 1s for the blocks where queens are placed

# naive algorithm
# Generate all possible configurations of queens on board and print a configuration that satisfies the given constraints

# backtracking algorithm
# The idea is to place queens one by one in different columns, starting from the leftmost column
# When we place a queen in a column, we check for clashes with already placed queens
#  In the current column, if we find a row for which there is no clash, we mark this row and column as part of the solution
# If we do not find such a row due to clashes then we backtrack and return false.

# giai thuat
# 1. Start in the leftmost column
# 2. If all queens are placed then return True
# 3. Try all rows in the current column
# Do following for every tried row
# - (a) if the queen can be placed safely in this row then mark this [row, column] as part
# of the solution and recursively check if placing queen here leads to a solution
# - if placing the queen in [row, column] leads to a solution then return true
# - if placing queen doesn't lead to a solution then unmark this [row, col] (backtrack)
# and go to the step (a) to try other rows
# 4. If all rows have been tried and nothing worked, return false to trigger backtracking

# Python3 program to solve N queen problems using backtracking
global N
N = 4


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


# A utility function to check if a queen can be placed on board[row][col]
# Note that this function is called when "col" queens are alreadly placed in columns
# from 0 to col -1
# So we need to check only left side for attacking queens
def isSafe(board, row, col):
    # check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col):
    # base case: if all queens are placed then return true
    if col >= N:
        return True

    # consider this column an try placing this queen in all rows
    # one by one
    for i in range(N):
        if isSafe(board, i, col):
            # place this queen in board[i][col]
            board[i][col] = 1
            # recursively to place rest of the queens
            if solveNQUtil(board, col + 1) == True:
                return True

            # if placing queen in board[i][col] doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in this column col then return false
    return False


def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


# Driver Code
solveNQ()
