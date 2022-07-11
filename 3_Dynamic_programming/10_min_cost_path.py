# Given a matrix cost[][] and a position (m,n) in cost[][]
# write a function that returns cost minimum cost path to reach (m,n) from (0,0)
# Each cell of matrix represents a cost to traverse through that cell
# Total cost of a path to reach (m,n) is the sum of all the coist on that path
# ( including source and destination)
# Can only traverse down, right and diagonally lower cells

# optimal substructure
# minCost(m, n) = min (minCost(m-1, n-1), minCost(m-1, n), minCost(m, n-1)) + cost[m][n]

# A naive recursive implementation of MCP problem
R = 3
C = 3
import sys


# return cost of minimum cost path from (0,0) to (m,n) in mat[R][C]
def minCost(cost, m, n):
    if n < 0 or m < 0:
        return sys.maxsize
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        return cost[m][n] + min(minCost(cost, m - 1, n - 1),
                                minCost(cost, m - 1, n),
                                minCost(cost, m, n - 1))


# A utility function that returns minimum of 3 intergers
def min(x, y, z):
    if x < y:
        return x if (x < z) else z
    else:
        return y if (y < z) else z


# Code to test the above function
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]


# print(minCost(cost, 2, 2))

# Overlapping subproblem: as we can see, MCP interatively compute base case
def minCostDP(cost, m, n):
    # intead of following line, we can use int tc[m+1][n+1] or dynamically allocate memory
    # to save space. The following line is used to keep the program simple
    tc = [[0 for x in range(C)] for x in range(R)]
    tc[0][0] = cost[0][0]

    # Do chi co the di theo 3 duong sang phai, doc xuong va cheo xuong nen co the tinh duoc cost cho duong ngang va doc
    # dau tien
    # Initialize first column of total cost array
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + cost[i][0]

    # Initialize first row of tc array
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + cost[0][j]

    # Construct rest of the tc array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i - 1][j - 1], tc[i - 1][j], tc[i][j - 1]) + cost[i][j]
    return tc[m][n]


# Driver program to test above functions
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minCostDP(cost, 2, 2))
