# Python3 for ternary search function.
# It will returns location of x in given array if it present, otherwise return -1

def ternarySearch(arr, l, r, x):
    if r >= l:
        mid1 = l + (r - l) // 3
        mid2 = mid1 + (r - l) // 3

        # if x present at the mid1
        if arr[mid1] == x:
            return mid1

        # if x present at the mid2
        if arr[mid2] == x:
            return mid2

        # check the left side
        if arr[mid1] > x:
            return ternarySearch(arr, l, mid1 - 1, x)

        # check the middle side
        if arr[mid2] < x:
            return ternarySearch(arr, mid2 + 1, r, x)

        # if x is present in middle
        return ternarySearch(arr, mid1 + 1, mid2 - 1, x)

    # return -1 if element is not present in array
    return -1


# initiation some settings
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = ternarySearch(arr, 0, n, x)

if result == -1:
    print("Element not found in the array")
else:
    print("Element is present at index %d" % result)
