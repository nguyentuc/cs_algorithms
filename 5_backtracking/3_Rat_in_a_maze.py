# A maze is given as N*N binary matrix of blocs where source block
# is upper left most block Ex: maze[0][0]
# destination block is lower rightmost block Ex: maze[N-1][N-1]
# A rat starts from source and has to reach the destination, the rat can move
# only in two directions: forward and down

# In the maze matrix, 0 means the block is a dead end and 1 mean the block can be
# used in the path from source to destination. Note that this is a simple version of the typical
# Maze problem.
# Some complex versions: rat can move in 4 directions and a more complex
# version can be with a limited number of moves

# Giai thuat
# 1. Create a solution matrix, initially filled with 0
# 2. Create a recursive function, which takes initial matrix, output matrix and position
# of rat (i, j)
# 3. If the position is out of the matrix or the position is not valid then return
# 4. Mark the position output[i][j] as 1 and check if the current position is destination or not
# If destination is reached print the output matrix and return
# 5. Recursively call for position (i+1, j) and (i, j+1)
# 6. Unmark position (i,j) ( output[i][j] = 0)

# Python 3 program to solve Rat in a Maze problem using backtracking
# maze size
N = 4


# A utility function to print solution matrix sol
def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + ' ', end="")
        print("")


# A utility function to check if x, y is valid index for N*N maze
def isSafe(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False


# This function solves the maze problems using backtracking. It mainly use
# solveMazeUtil() to solve the problem.
# It returns false if no path in the form if 1s

# A recursively utility function to solve Maze problem
def solveMazeUtil(maze, x, y, sol):
    # if (x, y is goal) return True
    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    # check if maze[x][y] is valid
    if isSafe(maze, x, y) == True:
        # mark x, y as part of solution path
        sol[x][y] = 1
        # move forward in x direction
        if solveMazeUtil(maze, x + 1, y, sol) == True:
            return True

        # if moving in x direction doesn't give solution the
        # move down in y direction
        if solveMazeUtil(maze, x, y + 1, sol) == True:
            return True
        # if none above movement work then
        # backtrack: unmark x, y
        sol[x][y] = 0
        return False


def solveMaze(maze):
    # creating a 4 * 4 of 2D list
    sol = [[0 for j in range(4)] for i in range(4)]
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist")
        return False
    printSolution(sol)
    return True


# Driver program to test above function
if __name__ == "__main__":
    # Initialising the maze
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]

    solveMaze(maze)

# Time complexity: O(2^(n^2))
# Space complexity: O(n^2): output matrix is required so an extra space of size
# n*n is needed
