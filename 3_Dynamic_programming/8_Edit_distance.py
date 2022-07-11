# Givem two strings str1 and str2 and below operations that can performed on str1
# Find minimum number of eidts required to convert str1 to str2
# Only using three type of operations
# Insert, Remove, Replace
# All three operations are equal cost

# Giai thuat
# Co the bat dau tu phia truoc hoa phia sau cua moi chuoi ky tu
# Neu di tu cuoi len
# - neu ky tu cuoi cung cua 2 chuoi giong nhau: bo qua va lap de quy voi
# 2 chuoi moi co do dai lan luot m-1 va n-1
# - con lai neu ky tu cuoi cung khong giong nhau, xem xet cac phep bien doi tren
# str1, thử tất cả 3 phép biến đỏi trên str1 và tính đệ quy chi phí tối thiểu cho cả 3 phép biến đổi và
# lấy giá trị nhỏ nhất
# insert: đệ quy cho m và n-1
# remove: đệ quy cho m-1 và n
# replace: đẹ quy cho m-1 và n -1

# A Naive recursive Python to find minimum number operations to convert str1 to str2
def editDistance(str1, str2, m, n):
    # if first string is empty, the only option is to insert all character
    # of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to remove all characters of first strings
    if n == 0:
        return m

    # If last characters of two strings are same, nothing much to do. Ignore last
    # characters and get count for remaining strings
    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)

    # if last chracters are not the same, consider all three operations on last
    # character of first string, recursively compute minimum cost for all
    # three operations and take minimum of three values
    return 1 + min(editDistance(str1, str2, m, n - 1),  # Insert
                   editDistance(str1, str2, m - 1, n),  # Remove
                   editDistance(str1, str2, m - 1, n - 1))  # Replace


# Initiliation code
str1 = "sunday"
str2 = "saturday"
print("Edit distance: ", editDistance(str1, str2, len(str1), len(str2)))
