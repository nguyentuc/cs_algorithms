# Given an undirected graph and a number m, determine if the graph can be
# coloured with at most m colours such that no two adjacent vertices
# of the graph are coloured with the same colour.
# Coloring of a graph means the assingment of colors to all vertices

# Input
# 1. A 2D array graph[V][V] where V is the number of vertices in graph and
# graph[V][V] is adjacency matrix representation of the graph.
# A value graph[i][j] is 1 there is a direct edge from i to j, otherwise is 0
# 2. An integer m which the maximum number of colors that can be used
# Output
# An array color[V] that should hace numbers from 1 to m, color[i] should represent
# the color assigned to the ith vertex
# The code should also return false if the graph cannot colored with m colors

# Method 1: Naive approaches
# Generate all possible configuration of colours. Since each node can be coloured using
# any of m available colours, the total number of colour configurations possible
# are m^V
# After generating colour or not, check if the adjacent vertices have the same colour or not
# If the conditions are met, print the combination and break the loop

# Algorithm
# 1. Create a recursive function that takes current index, number of vertices and output colour array
# 2. If the current index is equal to number of vertices. Check if the output colour configuration
# is safe ( check if the adjacent vertices does not have same colour)
# If the conditions are met, print configuration and break
# 3. Assign color to a vertex (1 to m)
# 4. For every assigned colour recursively call the function with next index and number of vertives
# 5. If any recursive function returns true break the loop and return true

# Number of vertices in the graph
# defined 4 4
# check if colored graph is safe or not
def isSafe(graph, color):
    # check for every edge
    for i in range(4):
        for j in range(i + 1, 4):
            if graph[i][j] and color[j] == color[i]:
                return False
    return True


# This function solves the m colouring problem using recursion. It returns
# false if the m colours cannot be assigned otherwise return true and print
# assigments of colurs to all vertices
# There may be more than one solutions, this function prints one of feasible solution
def graphColouring(graph, m, i, color):
    # if current index reached end
    if i == 4:
        # if colouring is safe
        if isSafe(graph, color):
            # print the solution
            printSolution(color)
            return True
        return False

    # Assign each color from 1 to m
    for j in range(1, m+1):
        color[i] = j
        # recursive 
# A utility function to print solution
def printSolution(color):
    print("Solution exists: Following are the assigned colours")
    for i in range(4):
        print(color[i], end=" ")

