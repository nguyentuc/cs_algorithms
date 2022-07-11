# Một bài toán DP có 2 thuộc tính: Overlapping Subproblems và
# optimal substructure
# Bài toán LIS sẽ đi tìm độ dài của chuỗi con dài nhất mà trong đó
# các thành phần trong chuỗi con là tăng dần
# VD: the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}
# Method 1: Recursion
# Optimal substructure:  arr[1..n] là đầu vào của mảng và L(i) là độ dài của LIS tại
# phần tử index i tương ứng với arr[i] là phần tử cuối cùng của LIS.

# A naive Python implementation of LIS problem
# To mak use of recursive calls, this function must return two things:
# 1, length of LIS ending with element a[n-1]. Use max_ending to represent
# 2, Overall maximum as the LIS may end with an element before  a[n-1], max_ref
# is use for this purpose
# The value of LIS of full array of size n is stored in max_ref which is final result

# global variable to store the maximum
global maximum


def _lis(arr, n):
    # to allow the access of global variable
    global maximum
    # base case
    if n == 1:
        return 1
    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1
    # recursively get all LIS ending with arr[0], arr[1],.. ,arr[n-2]
    # if arr[n-2] is smaller than arr[n-1] and max ending with arr[n-1] needs to be updated
    # then update it
    for i in range(1, n):  # tim LIS cho cac day tu 1 -> n -1
        res = _lis(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1
    # Compare maxEndingHere with overall maximum and update the overall
    # maximum if needed
    maximum = max(maximum, maxEndingHere)
    return maxEndingHere


def lis(arr):
    # to allow the access of global variable
    global maximum
    # length of arr
    n = len(arr)
    # maximum variable holds the result
    maximum = 1
    # the function _lis() stores its result in maximum
    _lis(arr, n)
    return maximum


# Initilization for test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print("Length of lis is:", lis(arr))
