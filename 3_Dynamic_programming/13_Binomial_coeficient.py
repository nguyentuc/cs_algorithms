# Hệ số nhị phân C(n,k) được định nghĩa là hệ số của x^k trong khai triển
# của (1+x)^n
# C(5,2): tim he so cua x^2 trong bieu thuc (1+x)^5

# Optimal substructure:
# C(n,k) = C(n-1,k-1) + C(n-1,k)
# C(n,0) = C(n,n) = 1

# Recursive Python implementation

def binomialCoeff(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # recursive call
    return binomialCoeff(n - 1, k - 1) + binomialCoeff(n - 1, k)


# Overlapping subproblems
# Dễ nhận thấ hàm trên lần lượt tính lại các subproblems nhiều lần
# Do dó bài toán Binomial coeficient có 2 tính chất của bài toán quy hoạch động
# A dynamic programming based pythn program that uses table C[][] to
# calculate the binomial coefficient
# time complexity and memory complexcity: O(n*k)
def DP_binomialCoef(n, k):
    C = [[0 for x in range(k + 1)] for x in range(n + 1)]
    # calculate value of Binomial coefficient in bottom up manner
    for i in range(n + 1):
        for j in range(min(i, k) + 1):  # tinh chat doi xung cua ma tran C(n,k)
            # base case
            if j == 0 or j == i:
                C[i][j] = 1

            # calculate value using previously stored values
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]


# Driver Program to test ht above function
n = 5
k = 2
print("Value of C(%d,%d) is (%d)" % (n, k,
                                     DP_binomialCoef(n, k)))
