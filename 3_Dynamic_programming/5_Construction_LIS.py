# Dynamic programming slution to construct Longest Increasing Subsequence
# Utility function to print LIS

def printLIS(arr: list):
    for x in arr:
        print(x, end=" ")
    print()


# Function to construct and print LIS
def constructPrintLIS(arr: list, n: int):
    # L[i]: the longest increasing subsequences end with arr[i]
    l = [[] for i in range(n)]

    # L[0] is equal to arr[0]
    l[0].append(arr[0])

    # start from index 1 (from 1 to n-1)
    for i in range(1, n):
        # do for every j less than i
        for j in range(i):
            if arr[i] > arr[j] and (len(l[i]) < len(l[j]) + 1):
                l[i] = l[j].copy()  # move l[j] into LIS at i

        # L[i] ends with arr[i]
        l[i].append(arr[i])

    # L[i] now stores increasing subsequence of arr[0,..i] that ends with arr[i]
    maxx = l[0]
    # LIS will be max of all increasing subsequence of arr
    for x in l:
        if len(x) > len(maxx):
            maxx = x

    # max will contain LIS
    printLIS(maxx)


# Initiliation code
if __name__ == "__main__":
    arr = [3, 2, 6, 4, 5, 1]
    n = len(arr)

    # construct and print LIS of arr
    constructPrintLIS(arr, n)
