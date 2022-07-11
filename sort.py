import random
import time


# Python program for implementation of Sort
class Sort(object):
    # Cac buoc thuc thi cua seletion sort
    # selection sort tim ra phan tu nho nhat cua mang cac unordered
    # sau do dich chuyen cac phan tu do vao mang cac ordered phan tu
    # thoi gian thuat toan la O(n^2)
    @staticmethod
    def selection(array):
        # Traverse through all array elements
        for i in range(len(array)):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i + 1, len(array)):
                if array[min_idx] > array[j]:
                    min_idx = j
            # Swap the found minimum element with the first element
            temp = array[i]
            array[i] = array[min_idx]
            array[min_idx] = temp

    # insertion sort
    # chon phan tu tu danh sach chua sap xep dua vao danh sach da sap xep
    # neu moi phan tu dua vao danh sach da sap xep deu lam cac phan tu trong ordered list dich chuyen
    # thoi gian: (1 + 2 + ... + n-1)c = O(n^2)
    # neu moi phan tu dua vao khong phai dich chuyen bat cu phan tu nao trong ordered list: O(n)
    # chi dich chuyen mot phan nho co dinh cac phan tu O(n)
    # dich chuyen mot luong n/2 cac phan tu: O(n^2)
    @staticmethod
    def insertionSort(array):
        # traverse through 1 to len(array)
        for i in range(1, len(array)):
            key = array[i]
            # move elements of arr[0,1,2,i-1] that greater than key
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

    @staticmethod
    def mergeSort(arr):
        if len(arr) > 1:
            # finding the mid of the array
            mid = len(arr) // 2
            # diving array element
            L = arr[:mid]
            R = arr[mid:]

            # sorting the left
            Sort.mergeSort(L)
            # sorting the right
            Sort.mergeSort(R)

            # merge
            i = j = k = 0
            # copy to the arr[] from the L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                elif L[i] > R[j]:
                    arr[k] = R[j]
                    j += 1
                else:
                    arr[k] = arr[k + 1] = R[i]
                    i += 1
                    j += 1
                    k += 1
                k += 1
            # checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    @staticmethod
    def printList(arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()


# Driver Code
if __name__ == '__main__':
    arr = []
    arr = random.sample(range(1, 50000), 900)
    start = time.time()
    print("Start:", start)
    print("Given array is", end="\n")
    Sort.printList(arr[:5])
    Sort.mergeSort(arr)
    print("Sorted array is: ", end="\n")
    Sort.printList(arr)
    print("End: ", time.time() - start)
