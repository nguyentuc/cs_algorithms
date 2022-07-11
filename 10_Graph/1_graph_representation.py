# A graph is a data structure that consists of the following two components:
# 1. A finite set of vertices also called as nodes.
# 2. A finite set of ordered pair of the form (u, v) called as edge
# The pair is ordered because (u, v) is not the same as (v, u) in case of a directed graph(di-graph).
# The pair of the form (u, v) indicates that there is an edge from vertex u to vertex v.
# The edges may contain weight/value/cost.

# Graphs are used to represent many real-life applications: Graphs are used to represent networks.
# The networks may include paths in a city or telephone network or circuit network.
# Graphs are also used in social networks like linkedIn, Facebook. For example, in Facebook,
# each person is represented with a vertex(or node). Each node is a structure and contains information like person id, name, gender, and locale.
# See this for more applications of graph.

# The following two are the most commonly used representations of a graph.
# 1. Adjacency Matrix
# 2. Adjacency List

# Python program to demonstrate the adjacency list representation of the graph

"""
A Python program to demonstrate the adjacency
list representation of the graph
"""


# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

        # Function to add an edge in an undirected graph

    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

        # Function to print the graph

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

        # Driver program to the above graph class


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
