# Check two given line segments intersect
# Given two line segments (p1, q1) and (p2, q2)
# find if the given line segments intersect with each other

#  A pytho3 program to find if 2 given line segments
# intersect or not

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# given three colinear points p, q, r the function check if point q lies on
# line segment 'pr'
def onSegment(p, q, r):
    if q.x <= max(p.x, r.x) and (q.x >= min(p.y, r.y)) and (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y)):
        return True
    return False


def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values
    # 0: colinear points
    # 1: clockwise point
    # 2: counter clockwise

    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if val > 0:
        return 1
    elif val < 0:
        return 2
    else:
        return 0


# the main function that returns true if the line segment 'p1q1' and 'p2q2' intersect
def doIntersect(p1, q1, p2, q2):
    # find the 4 orientations required for the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True

    # Special Cases

    # p1 , q1 and p2 are colinear and p2 lies on segment p1q1
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True

    # p1 , q1 and q2 are colinear and q2 lies on segment p1q1
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True

    # p2 , q2 and p1 are colinear and p1 lies on segment p2q2
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True

    # p2 , q2 and q1 are colinear and q1 lies on segment p2q2
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True

    # If none of the cases
    return False


# Driver program to test above functions:
p1 = Point(1, 1)
q1 = Point(10, 1)
p2 = Point(1, 2)
q2 = Point(10, 2)

if doIntersect(p1, q1, p2, q2):
    print("Yes")
else:
    print("No")

p1 = Point(10, 0)
q1 = Point(0, 10)
p2 = Point(0, 0)
q2 = Point(10, 10)

if doIntersect(p1, q1, p2, q2):
    print("Yes")
else:
    print("No")

p1 = Point(-5, -5)
q1 = Point(0, 0)
p2 = Point(1, 1)
q2 = Point(10, 10)

if doIntersect(p1, q1, p2, q2):
    print("Yes")
else:
    print("No")
