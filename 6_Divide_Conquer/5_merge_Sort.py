# Python3 program to count inversion in an array
# function to use inversion count
def mergeSort(arr, n):
    # temp_arr is create to store sorted array in merge function
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


# this function will use MergeSort to count inversion
def _mergeSort(arr, temp_arr, left, right):
    # a variable inv_count is used to store inversion counts in each
    # recursive call
    inv_count = 0
    # we will make a recursive call if and only if we have more than one elements
    if left < right:
        # mid is calculated to divide the array into two subarrays
        # floor division is must in case of python
        mid = (left + right) // 2
        # it will calculate inversion count in the left subarray
        inv_count += _mergeSort(arr, temp_arr, left, mid)
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)
        # it will merge two subarrays in a sorted subarray
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


# this function will merge two subarrays int a single sorted subarray
def merge(arr, temp_arr, left, mid, right):
    i = left  # starting indx of left array
    j = mid + 1  # starting index of right array
    k = left  # starting index of to be sorted subarray
    inv_count = 0

    # condidioon are check to make sure that is and j don't exceed their subarray
    while i <= mid and j <= right:
        # there will be no inversion of arr[i] <= arr[j]
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # inversion will occur
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1
    # copy the remaining elemtnst of left subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # copy the remaining elements of right subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count

# driver code
# given array is
arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are: ", result)
