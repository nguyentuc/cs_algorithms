# Given a sequence of matrices, find the most efficient way to multiply these matrices together
# The problems is not actually to perform the multiplications, but merely to decide in which
# order to perform the multiplications
# We have many options to multiplu a chain of matrices because matrix
# multiplication is assosiative.
# (ABC)D = (AB)(CD) = A(BCD) =...

# Optimal substructure
# A simple solution is to place parenthesis at all possible places
# calculate the cost for each placement and return the minimum value
# In a chain of matrices of size n, we can place the first set  of
# parenthesis in n-1 ways.
# When we place a set of parenthesis we devide the problem into subproblems
# of smaller size. Therefore the problem has optimal substructure property and
# can be easily sooved using recursion

# Overlapping subproblems
# Following is a recursive implementation
# that simply follows the above optimal substructure property

# A naive recursive implement that simply follow the above optimal substructure
import sys


# matrix A[i] has dimension p[i-1] x p[i]
# for i = 1..n

def MatrixChainOrder(p, i, j):  # i,j la index cua p
    if i == j:
        return 0
    _min = sys.maxsize

    # place parenthesis at different places between first and last matrix
    # recursively calculate count of multiplications for each parenthesis
    # placement and return the minimum cost
    for k in range(i, j):
        count = (MatrixChainOrder(p, i, k) + MatrixChainOrder(p, k + 1, j)
                 + p[i - 1] * p[k] * p[j])
    if count < _min:
        _min = count
    return _min


# Driver code
arr = [1, 2, 3, 4, 3]
n = len(arr)

print("Minimum number of multiplications is ",
      MatrixChainOrder(arr, 1, n - 1))


# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm
def DP_matrix_chain_order(p, n):
    # For simplicity of the program,
    # one extra row and one
    # extra column are allocated in m[][].
    # 0th row and 0th
    # column of m[][] are not used
    m = [[0 for x in range(n)] for x in range(n)]

    # m[i, j] = Minimum number of scalar
    # multiplications needed
    # to compute the matrix A[i]A[i + 1]...A[j] =
    # A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0

    # L is chain length.
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):

                # q = cost / scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n - 1]


# Driver code
arr = [1, 2, 3, 4]
size = len(arr)

print("Minimum number of multiplications is " +
      str(DP_matrix_chain_order(arr, size)))
