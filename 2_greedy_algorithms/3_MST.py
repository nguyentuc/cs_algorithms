# Cây bao trùm nhỏ nhất: cho trước một đồ thị vô hướng, môt cây bao trùm
# là cây kết nối tất cả các đỉnh lại với nhau.
# Một đồ thị có thể có nhiều cây bao trùm khác nhau
# Cây bao trùm nhỏ nhất là cây bao trùm mà tổng tọng số nó nhỏ hơn hoặc bằng
# trọng số của tất cả các cây bao trùm khác.
# Trọng số của cay bao trùm được tính bởi tổng tất cả các trọng số trên
# cạnh của nó.
# Một cây bao trùm trên tập V đỉnh thì sẽ có V-1 cạnh

# Giải thuật tìm cây bao trùm nhỏ nhất của KruKal
# 1. Sắp xếp tất cả các cạnh theo chiều không giảm của trọng số
# 2. Chọn cạnh có weight nhỏ nhất. Nếu nó tao thành chu kỳ với trong cây bao trùm
# thì loại, ngược lại thì chọn.
# 3. Lặp bước 2 cho đến khi có V-1 cạnh trong cây MST

# Ở bước 2: Dùng giải thuật Union-Find để xác định có chu trình trong đồ thị
# Giải thuật này là tham lam với bước tham lam là chọn ra cạnh có trọng số nhỏ nhất mà không tạo
# thành chu trình trong cây.

# Python program for Kruskal algorithm to find MST ò a given connected
# undiredted and weighted graph
from collections import defaultdict


# Class to epresent a graph
class Graph:
    def __init__(self, verices):
        self.V = verices  # number of vertices
        self.graph = []
        # default dict to store a graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # uses path compression technique
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # attach smaller rank tree under root of rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # if ranks are same, then make one as root and increment its rank by one
        else:
            parent[yroot] = xroot  # chon xroot lam node cha va tang rank len 1
            rank[xroot] += 1

    # the main fuction to contruct MST using Kruskal's algorthm
    def KruskalMST(self):
        # this will store the resultant MST
        result = []
        # an index variable, used for sorted edges
        i = 0
        # an index variable, used for result
        e = 0

        # step1: sort all the edges in non-decrease order.
        # It we are not allow to change the given graph, we can create a new copy of graph
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        # create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            # step 2: Pick the smallest edge and increment the index for next interation
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if including this edge doesn't cause a cycle, include it in result
            # and increment the index of result for next edge

            if x != y:
                e = e + 1
                result.append([u, v, w])
                # neu canh do duoc chon thi tao cay MST
                self.union(parent, rank, x, y)
            # else discard the edge
        minimumCost = 0
        print("Edge in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)


# initilization
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(0, 3, 15)
g.addEdge(2, 3, 4)
g.KruskalMST()
