# There are two sorted array A, B
# Write an algorithm to find the median of the array obtain after merging the above
# two array

# The size of the set for which we are looking for the median is even (2n)
# we need to take the average of middle two numbers and return floor of the average

# Method 1: Simply count while merging
# Use merge procedure of merge sort. Keep track on count while comparing elements of two
# array. If count becomes n(For 2n elements),
# we have reached the median. Take the average of the elements at indexes n-1 and n in the merged array

# Both arr1, arr2 are sorted arrays
# Both have n elements
def getMedian(arr1, arr2, n):
    i = 0
    j = 0
    m1 = m2 = -1
    # since there are 2n elements, median will be average of elements
    # at index n - 1 and n in the array obtained after merging arr1, arr2

    count = 0
    while count < n + 1:
        count += 1

        # below is to handle case where all elements of arr1[] are smaller
        # than smallest element of arr2
        if i == n:
            m1 = m2
            m2 = arr1[0]
            break

        # equals sign because if two arrays have common elements
        if arr1[i] <= arr2[j]:
            m1 = m2  # Store the prev median
            m2 = arr1[i]
            i += 1
        else:
            m1 = m2  # Store the prev median
            m2 = arr2[j]
            j += 1
    return (m1 + m2) / 2


# Driver code to test above function
ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]
n1 = len(ar1)
n2 = len(ar2)
if n1 == n2:
    print("Median is ", getMedian(ar1, ar2, n1))
else:
    print("Doesn't work for arrays of unequal size")


# Time complexity is: O(n)

# Method 2: By comparing the medians of two arrays
# Using divide and conquer we divide the 2 arrays accordingly recursively till
# we get two elements in each array, hence then we calculate median

# condition len(arr1) = len(arr2) = n
def getMedian(arr1, arr2, n):
    # there is no element in any array
    if n == 0:
        return -1

    # 1 element in each
    elif n == 1:
        return (arr1[0] + arr2[0]) / 2

    elif n == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2

    else:
        # calculating medians
        m1 = median(arr1, n)
        m2 = median(arr2, n)

        # then the elements at median
        # position must be between the
        # greater median and the first
        # element of respective array and
        # between the other median and
        # the last element in its respective array.
        if m1 > m2:

            if n % 2 == 0:
                return getMedian(arr1[:int(n / 2) + 1],
                                 arr2[int(n / 2) - 1:], int(n / 2) + 1)
            else:
                return getMedian(arr1[:int(n / 2) + 1],
                                 arr2[int(n / 2):], int(n / 2) + 1)

        else:
            if n % 2 == 0:
                return getMedian(arr1[int(n / 2 - 1):],
                                 arr2[:int(n / 2 + 1)], int(n / 2) + 1)
            else:
                return getMedian(arr1[int(n / 2):],
                                 arr2[0:int(n / 2) + 1], int(n / 2) + 1)


def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n / 2)] +
                arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n / 2)]


# Driver code
arr1 = [1, 2, 3, 6]
arr2 = [4, 6, 8, 10]
n = len(arr1)
print(int(getMedian(arr1, arr2, n)))
