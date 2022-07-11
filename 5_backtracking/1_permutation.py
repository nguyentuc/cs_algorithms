# Thuạt toán quay lui
# Quay lui là một kỹ thuật để thiết kế giải thuật dựa trên đệ quy.
# Ý tưởng của quay lui là tìm lời giải từng bước, mỗi bước chọn một trong số
# các lựa chọn khả dĩ và đệ quy.

# Tư tưởng
# Dùng trong bài toán liệt kê các cấu hình. Mỗi cấu hình được xây dựng bằng
# từng phần tử. Mỗi phần tử lại được chọn bằng cách thử các khả năng
# Các bước trong liệt kê cấu hình dạng X[1..n]
# - Xét tất cả các giá trị X[1] có thể nhận, thử X[1] nhận các giá trị đó, với mỗi X[1]
# - Xét tất cả các giá trị X[2] có thể nhận, thử X[2] cho các giá trị đó. Với mỗi giá trị X[2]
# lại xét các giá trị của X[3] và tiếp tục cho đến bước n
# - thông báo cấu hình tìm được
# bản chất quay lui là tìm kiếm theo chiều sâu
# Mã giả cho thuật toán quay lui
# Backtracking(k) {
# 	for([Mỗi phương án chọn i(thuộc tập D)]) {
# 		if ([Chấp nhận i]) {
# 			[Chọn i cho X[k]];
# 			if ([Thành công]) {
# 				[Đưa ra kết quả];
# 			} else {
# 				Backtracking(k+1);
# 				[Bỏ chọn i cho X[k]];
# 			}
# 		}
# 	}
# }

# A permutation, also called an “arrangement number” or “order,” is
# a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself.
# A string of length n has n! permutation.

# Python program to print all permutations with duplicates allowed

def toString(List):
    return ''.join(List)


# function to print permutations of string. This function takes three parameters
# string
# starting index of the string
# ending index of the string
def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


# driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)

