# Prim là thuật toán tham lam, bắt đầu từ cây trống
# Ý tưởng: duy trì 2 tập các đỉnh
# Tập 1: các đỉnh đã có trong MST
# Tập 2: Các đỉnh chưa được đưa vào MST
# Tại mỗi bước, sẽ xem xét tất cả các cạnh liên kết 2 tập và chọn ra cạnh với trọng
# số nhỏ nhất để kết nối 2 tập

# Ý tưởng: chia làm 2 tập (trong MST và ngoài MST), tại mỗi bước tìm ra
# cạnh nối 2 tập này có trọng số nhỏ nhất, và đưa đỉnh đó vào tập trong MST

# Giải thuật
# 1. Tạo một mstSet bao gồm tất cả các đỉnh trong MST
# 2. Chọn ra một giá trị key cho tất cả các đỉnh, khởi tạo giá trị ban đầu là vô cùng
# gán key = 0 nếu đó là đỉnh đầu tiên được đưa vào MST
# 3. Khi mstSet không chứa tất cả các đỉnh
# - Chọn một đỉnh u không có trong mstSet và có giá trị key nhỏ nhất
# - đưa u vào mstSet
# - Cập nhật giá trị key cho tất cả đỉnh liền kề của u, đối với tất cả
# các đỉnh liền kề v, nếu trọng số của cạnh u-v nhỏ hơn  nhỏ hơn keys tại v
# thì update key tại v là trọng số của cạnh u-v
# trọng số cạnh là chi phí để kết nối 2 cạnh, trọng số của đỉnh là chi phí để
# đi từ gốc đến đỉnh đó

# Python program for PrimMST algorithms
import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function o print the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(parent[i], '-', i, '\t', self.graph[i][parent[i]])

    # A utility fuction to find vertex with minimum distance value, from the
    # set of vertices not yet include in shortest path tree
    def minKey(self, key, mstSet):
        # Initilaize min value
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    # Function to construct and print MST for a graph represent using adjacency matrix
    # representation
    def primMST(self):
        # Key value used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        # An array to store constructed MST
        parent = [None] * self.V
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1  # First node choose as root
        for count in range(self.V):
            # pick minimum distance vertex from the set of vertex outside MST
            u = self.minKey(key, mstSet)
            # Put th minimum distance vertex in the shortest path tree
            mstSet[u] = True
            # Update dist value of adjacent vertices of the picked vertex only
            # if the current distance is greater than new distance
            # and vertex not in the shortest path tree
            for v in range(self.V):
                # graph[u][v] is non-zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet include in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]
g.primMST()
