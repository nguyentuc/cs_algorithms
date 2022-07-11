# Inversion Count for an array indicates – how far (or close) the array is from being sorted.
# If array is already sorted then inversion count is 0.
# If array is sorted in reverse order that inversion count is the maximum
# Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

# Method 1: Simple
# time complexity: O(n^2): two nested loops are needed to traverse the array
# from start to end.
# Space complexity O(1) no extra place is required
# Python3 program to count inversions in an array
def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count


# Driver code
arr = [1, 20, 6, 4, 5]
n = len(arr)
print("Number of inversions are: ", getInvCount(arr, n))
