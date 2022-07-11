# Simple solution: using nested loop

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
print("Number of inversion are: ", getInvCount(arr, n))


# Using MergeSort to count inversion
# Time complexity: o(nlog(n))
# Space complexity: O(n)

# function to use inversion count
def mergeSort(arr, n):
    # A temp_arr is created to store sorted array in merge function
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


# this function will use MergeSort to count inversions
def _mergeSort(arr, temp_arr, left, right):
    # A variable inv_count is used to store inversion counts in each
    # recursive call
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += _mergeSort(arr, temp_arr, left, mid)
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


# this function will merge two subarray
# in a single sorted subarray
def merge(arr, temp_arr, left, mid, right):
    i = left  # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.

    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    return inv_count


# Driver Code
# Given array is
arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)
