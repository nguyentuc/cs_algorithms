# Returns index of x in arr if present, else -1
class BinarySearch(object):
    @staticmethod
    def recursion(elements, l, r, x):
        if r >= l:
            mid = l + (r - l) // 2
            # If element is present at the middle itself
            if elements[mid] == x:
                return mid
            # can only be present in left subarray
            elif elements[mid] > x:
                return BinarySearch.recursion(elements, l, mid - 1, x)
            # Else the element can only be present in right subarray
            else:
                return BinarySearch.recursion(elements, mid + 1, r, x)
        else:
            # Element is not present in the array
            return -1

    @staticmethod
    def iterative(elements, l, r, x):
        while l <= r:
            mid = l + (r - l) // 2

            # Check if x is present at mid
            if elements[mid] == x:
                return mid

            # If x is greater, ignore the left ones
            elif elements[mid] < x:
                l = mid + 1

            # If x is smaller, ignore right ones
            else:
                r = mid - 1

        # the element was not present
        return -1


# Driver Code
arr = [2, 3, 4, 10, 40, 68, 98]
x = 40

# Recursion call
result = BinarySearch.recursion(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

# Interative call
result = BinarySearch.iterative(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")