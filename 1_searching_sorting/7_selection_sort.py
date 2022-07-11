# Python3 implement for selection sort
# tim phan tu nho nhat va doi cho cho phan tu dau tien
# lap lai cho den khi tat ca phan tu duoc duyet
A = [64, 25, 12, 22, 11]

for i in range(len(A)):
    # find the minimum element in remaining unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    # swap the found minimum element with the first element
    A[i], A[min_idx] = A[min_idx], A[i]

# initiation some  settings
print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i])
