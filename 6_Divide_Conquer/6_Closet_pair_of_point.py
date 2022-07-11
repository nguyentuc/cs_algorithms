# Brute force solution is O(n^2)
#  O(n x (Logn)^2) approach is discussed
# the smallest distance in O(nLogn) time using Divide and Conquer

# Divide and conquer program in python3 to find the smallest distance from
# given set of point
import math
import copy


# A class to represent a point in 2D plane
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# A utility function to find the distance between two points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


# Brute force method to return the smallest distance between two points in P
# of size n
def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
    return min_val


# Function to find the distance between the closet points of strip of given size
# All point are sorted accord in y coordinate
# They all have an upper bound on minimum distance as d
def stripClosest(strip, size, d):
    # initialize the minimum distance
    min_val = d

    # pick all points one by one and try next points till the difference
    # between y coordinates is smaller than d
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
    return min_val


# A recursive function to find the smallest dist
# The array P contains all points sorted according to x coordinate
def closestUtil(P, Q, n):
    # if there are 2 or 3 points then use brute force
    if n <= 3:
        return bruteForce(P, n)

    # find the middle point
    mid = n // 2
    midPoint = P[mid]

    # Consider the vertical line passing through the middle point calculate
    # the smallest distance dl on left of middle point and dr on the right side
    dl = closestUtil(P[:mid], Q, mid)
    dr = closestUtil(P[mid:], Q, n - mid)

    # find the smaller of two distance
    d = min(dl, dr)
    # build an array strip[] that contains point closer than d
    # to the line passing through the middle point
    strip = []
    for i in range(n):
        if abs(Q[i].x - midPoint.x) < d:
            strip.append(Q[i])
    # find the closest points in strip and return the minimum of d and closest distance in strip[]
    return min(d, stripClosest(strip, len(strip), d))


# the main fuction that finds the smallest distance
# this method mainly uses closestUtil()
def closest(P, n):
    P.sort(key=lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key=lambda point: point.y)

    # Use recursive function closestUtil() to find the smallest distance
    return closestUtil(P, Q, n)


# Driver code
P = [Point(2, 3), Point(12, 30),
     Point(40, 50), Point(5, 1),
     Point(12, 10), Point(3, 4)]
n = len(P)
print("The smallest distance is",
      closest(P, n))
