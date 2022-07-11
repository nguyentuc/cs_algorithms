# There are many subproblems in above recursive solution which are solved again and
# again. This problems has overlapping substructure property and recomputation of the same
# problem can be avoided by either using Memoization or Tabulation
# Ex: arr[] = {3, 10, 2, 11}
# arr[2] > arr[1] {LIS[2] = max(LIS [2], LIS[1]+1)=2}
# arr[3] < arr[1] {No change}
# arr[3] < arr[2] {No change}
# arr[4] > arr[1] {LIS[4] = max(LIS [4], LIS[1]+1)=2}
# arr[4] > arr[2] {LIS[4] = max(LIS [4], LIS[2]+1)=3}
# arr[4] > arr[3] {LIS[4] = max(LIS [4], LIS[3]+1)=3}

# Dynamic programming Python implementation of LIS problem
# lis returns length of the longest increasing subsequence in arr of size n

def lis(arr):
    n = len(arr)
    # Delare the list for LIS and initialize LIS values for all indexes
    lis = [1] * n
    # compute optimized  LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Initialize maximum to 0 to get the maximum of all LIS
    maximum = 0
    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


# Initilization to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of LIS is:", lis(arr))
