# Code python3 to implement Jump search
import math


def jumpSearch(arr, x, n):
    # finding block size to be jump
    step = math.sqrt(n)
    # find theo block where element is present
    prev = 0
    while arr[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    # arr[prev:] have x
    # do the linear search for x in block begin with prev
    while arr[int(prev)] < x:
        prev += 1
        # if we reached next block or end of array, element is not present
        if prev == min(step, n):
            return -1
    # if element is found
    if arr[int(prev)] == x:
        return prev

    return -1


# init some settings
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610]
x = 55
n = len(arr)

# finding the index of x using Jump search
index = jumpSearch(arr, x, n)

# print the index where x is located
print("Number", x, "is at index", "%.0f" %index)

