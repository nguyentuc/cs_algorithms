# Python3 code for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        # finding the mid of the array
        mid = len(arr) // 2

        # dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
        # sorting two halves
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        # copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # checking if any element was left (the left ones)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):  # check the element was left in the right ones
            arr[k] = R[j]
            j += 1
            k += 1


arr = [12, 11, 13, 5, 6, 7]
print("Given array is: ", arr)
mergeSort(arr)
print("Sorted array is: ", arr)

