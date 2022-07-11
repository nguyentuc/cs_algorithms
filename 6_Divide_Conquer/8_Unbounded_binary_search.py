# Given a monotonically increasing fucntion f(x) on the non-negative intergers
# find the value of x where f(x) become positive for the first time

# simple solution is to consider all positive numbers starting from 0 and
# find the first number for which f(x) is positive
# time complexity is: O(x)


# O(log(x)) by using binary search algorithm
# We cannot apply standard binary search on an unbounded search space
# since we dont know upper limit of search space
# Use exponential search to detemine the range of x and performe binary search in that range
# Exponential search starts with i = 1 and  keep doubling i until f(i) become
# positive  for the first time
# when f(i) becomes positive, perform a binary search within the search space [i/2; i]

# A monotonically increasing function f(x) = 3x - 100
def f(x):
    return 3 * x - 100


# find the value of x in the search space [low, high] using BS
# where f(x) becomes positives for the first time
def binarySearch(low, high):
    # base condition
    if high < low:
        return -1
    # find the mid-value in the search space
    mid = low + ((high - low) / 2)
    if f(mid) > 0:
        if mid == low or f(mid - 1) <= 0:
            return mid
        return binarySearch(low, mid - 1)


# Returns the positive value `x`, where `f(x)` becomes positive for the first time
def exponentialSearch():
    # find the range in which the result would reside
    i = 1
    while f(i) <= 0:
        # calculate the next power of 2
        i *= 2

    # call binary search on `[i/2, i]`
    return binarySearch(i / 2, i)


if __name__ == '__main__':
    x = exponentialSearch()
    print("f(x) becomes positive for the first time when x =", int(x))
