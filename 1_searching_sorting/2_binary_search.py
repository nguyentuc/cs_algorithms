# Python3 program for recursive binary search
# return index of x if x in array, else return -1

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        # if element is present at the middle itself
        if arr[mid] == x:
            return mid

        # check the left
        elif arr[mid] > x:
            return binarySearch(arr, l, mid -1, x)

        # check the right
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

# init some settings
arr = [2, 3, 4, 10, 40]
x = 10
# run algorithm
result = binarySearch(arr, 0, len(arr) -1, x)
if result != -1:
    print("Element is present at index %d" %result)
else:
    print("Element is not present in array")
