# bài toán ngựa đi tuần
# cho một quân mã trên bàn cơ vua, tìm ra các bước đi của quân mã
# sao cho tại mỗi ô nó chỉ đi một lần

# Giải thuật
# Nếu tất cả các vị trí đều được thăm: in ra đường đi đến các vị trí đó
# Nếu không:
# - Add one of the next moves to solution vector and reucrsively check if
# this move leads to a solution. ( A knight can make maximum eight moves, we
# choose in the above step doesn't lead to a solution)
# - If the move chosen in the above step doesn't lead to a solution then
# remove this move from the solution vector and try other alternative moves
# - If none of the alternatives work then return false
# (Returning false will remove the previous added items in recursion and if false is
# returned by initial call of recursion ten "no solution exits"

# Python3 program to solve Knight Tour problem using Backtracking
# chessboard size
n = 8


def isSafe(x, y, board):
    # A utility function to check if i,j are valid indexes for N*N chessboard
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
        return True
    return False


def printSolution(n, board):
    # A utility function to print Chessboard matrix
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solveKT(n):
    # This function solves the Knight tour problem using backtracking
    # This function mainly uses solveKTUlti() to solve the problem.
    # It returns false if no completetour is possible, otherwise return
    # true and prints the tours
    # Please note that there may be more than one solutions, this function prints one
    # of the feasible solutions

    # Initialization of board matrix
    board = [[-1 for i in range(n)] for i in range(n)]
    # move_x and move_y define next move of Knight
    # move_x, move_y are next value of x, y coordinate respectively

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the knight is initially at the first block
    board[0][0] = 0
    # board[0][7] = 0
    # Step counter for knight's position
    pos = 1

    # checking if solution exists or not
    if not solveKTUtil(n, board, 0, 0, move_x, move_y, pos):
        print("Solution does not exist")
    else:
        printSolution(n, board)


def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    # A recursively utility function to solve Knight tour problem
    if pos == n ** 2:
        return True

    # Try all next moves from the current coordinate x,y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if isSafe(new_x, new_y, board):
            board[new_x][new_y] = pos
            if solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos + 1):
                return True

            # Backtracking
            board[new_x][new_y] = -1
    return False


# Driver code
if __name__ == "__main__":
    solveKT(n)

# There are N^2 cell for each and we have a maximum of 8 possible moves to choose
# from, so the worst running time is O(8^(N^2))
