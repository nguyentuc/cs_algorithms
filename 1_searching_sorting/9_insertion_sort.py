# Python3 program for implement of Insertion Sort

def insertionSort(arr):
    # traverse through the array
    for i in range(1, len(arr)):
        # chon mot phan tu vao trong danh sach con sap xep
        key = arr[i]
        # move elements of arr[0,1,2,i-1] that greater than key
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
