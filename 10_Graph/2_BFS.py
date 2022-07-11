# Python3 program to print BFS traversal from a given source vertex
# BFS(int s) traverses vertices reachable from s

from collections import defaultdict


# this class represents a directed graph using adjacncy list representation
class Graph:
    # constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # function to print a BFS of a graph
    def BFS(self, s):
        # mark all vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # create a queue for BFS
        queue = []
        # mark the source node as visited and queue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # get all adjacent vertices of the dequeued vertex s. If a adjacent
            # vertices of the qequed vertex s.
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
