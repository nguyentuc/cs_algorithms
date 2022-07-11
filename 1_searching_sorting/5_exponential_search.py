# Python code to find an element x in a sorted array using Exponential Search
# giai thuat de quy tim ra vi tri cua x trong mang arr
# neu co tra ve vi tri cua no, neu khong tra ve -1
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + int((r - l) / 2)
        # if the element is present at middle of itself
        if arr[mid] == x:
            return mid

        # if the element is smaller than mid, then it can only present in
        # the left of subarray
        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # else the element can only be present in the right
        return binarySearch(arr, mid + 1, r, x)
    return -1


# return the position of first occurrence of x in array
def exponentialSearch(arr, n, x):
    # if x is present at first localtion itself
    if arr[0] == x:
        return 0

    # find range for binary search
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    # call binary search for the found range
    return binarySearch(arr, int(i / 2), min(i, n - 1), x)


# initiation some settings
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponentialSearch(arr, n, x)

if result == -1:
    print("Element not found in the array")
else:
    print("Element is present at index %d" % result)
