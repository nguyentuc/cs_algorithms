# Note: sắp xếp vun đống: một kỹ thuật sắp xếp phân loại dựa trên
# đống nhị phân
# tương tự sắp xếp chọn: phần tử lớn nhất được sắp xếp vào cuối danh sách
# mỗi mảng có thể được coi là một đống nhị phân
# xay dung dong nhi phan:
# một mảng a[1..n] có thể xem là một cây nhị phân với gốc là phần tử thứ nhất
# node con bên trái của đỉnh a[i] là a[2i], node con bên phải là a[2i+1]
# nếu mảng bắt đầu bằng 0 (a[0..n-1]) thì phần tử đầu tiên là a[i] và các node
# con trái phải tương ứng là a[2i+1] và a[2i+2]
# những node có index > (int) n/2 không có node con (node lá)

# nếu khóa của phần tử cha luôn lớn hơn bằng khóa trên các node con thì
# đống đó được gọi là đống cục đại (phần tử đầu tiên trong đống cực đại là lớn nhất)

# ngược lại được gọi là đống cực tiểu

# thuật toán vun đống là tim cách sắp xếp lại các phần tử của mảng ban đầu thành đống

# để vun một mảng thành đống ta sẽ thực hiện vun từ dưới lên bắt đầu từ
# phần tử a[int(n/2)] đến a[1]

# sắp xếp bằng vun đống
# sau khi mảng đã là đống, lấy phần tử đầu tiên trên đỉnh của đống và đưa vào vị trí cuối cùng
# chuyển hóa phần tử cuối cùng lên đỉnh đống
# tiếp tục vun lại đống với mảng n-1 phần tử và cũng lấy phần tử đầu tiên đưa
# đống vào cuối cùng của mảng
# lặp lại cho đến khi đống chỉ còn lại một phần tử

# cài đặt
# Python program for implementation of heap sort
# to heapify subtree rooted at index i
# n is size of heap
def heapify(arr, n, i):
    largest = i  # initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2
    # if left child of root exits and is greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # if right child of root exits and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # change root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # heapify the root
        heapify(arr, n, largest)


# the main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
    # build a maxheap (tim phan tu lon nhat sau do tach ra luu noi khac)
    for i in range(n // 2 - 1, -1, -1):  # mang tu n//2 den 0
        heapify(arr, n, i)

    # one by one extract elements and rebuild a minheap
    for i in range(n - 1, 0, -1):  # mang tu n-1 den 1
        arr[i], arr[0] = arr[0], arr[i]  # doi cho phan tu cuoi va phan tu dau (thu duoc phan tu cuoi la max)
        heapify(arr, i, 0)  # vun lai mang moi voi kich thuoc nho ho


# initilization some values
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Sort array: ", arr)
