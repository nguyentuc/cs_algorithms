# LCS problem:
# Given two sequences, find the length of longest subsequence present in both
# of them. A subsequence is a sequence that appears in the same relative order, but not necessary
# contiguous.

# Giai thua ngay tho nhat la dua ra tat ca cac subsequence roi sau do tim ra subsequence nao
# chung giua 2 chuoi va co do dai lon nhat
# Phan tich do phuc tap thoi gian:
# Neu su dung phuong phap vet can thi de tim duoc so chuoi con trong mot chuoi co the
# la C1n + C2n +... +Cnn = 2^n - 1
# thoi gian de kiem tra mot chuoi con co cung ton tai trong ca 2 chuoi la o(n)
# => tong thoi gian : O(2^n x n)

# Co duoc ung dung trong cac bai toan lien quan den tin sinh

# LCS problem has optimal substructure property (Optimal substructure) and overlapping subproblems

# A naive recursive implement of Lcs problem
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))


# Initialization code to test the above function:
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y, len(X), len(Y)))

# cai dat nay worst case O(2^n)
