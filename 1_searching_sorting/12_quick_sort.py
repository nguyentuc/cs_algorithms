# mergesort và quicksort là hai thuật toán chia để trị
# Quicksort sẽ chọn ra một điểm làm pivot và sau đó tiến hành sắp xếp trên các
# thành phần
# có nhiều cách chọn pivot khác nhau: đầu, giữa, cuối, hoặc bất kỳ

# Python program for implementation of QuickSort
# In this function, last element chosen as pivot
# All the elements are smaller than pivot will be place in the left
# All element are bigger will place to the right of the pivot
import random
def partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot = arr[high]

    for j in range(low, high):  # j =[low, high -1]
        # if current element is small than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    # khi duyet het ta ca cac phan tu co gia tri nho hon pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # doi cho a[pivot] vao dung vi tri cua no
    return i + 1
    # thu duoc mang arr[low-1; i+1] da duoc sap xep


# the main function implements QuickSort
# arr[] => array to be sorted
# low => starting index
# high => ending index

# function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at the right place
        pi = partition(arr, low, high)

        # separately sort elements before and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Initiation value for function
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array:", arr)
