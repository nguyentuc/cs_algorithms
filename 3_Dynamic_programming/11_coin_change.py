# Given value N, if we want to make change N cents
# have infinite of each of S ={S1,S2,..,Sm} valued coins
# how many ways can we make the change? the order of coins doesn't matter
# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
# So output should be 4

# Optimal substructure:
# 1. To count the total number of solutions, we can divide all set solutions into two sets
# - solutions that do not contain mth coin
# - solutions that contain at least one Sm
# Let count(S[], m,n) be the function to count the number of solutions, then it can
# be written as sum of count(S[],m-1, n) and count(S[], m, n - Sm)

# Recursive Python3 program for coin change problem
# Returns the count of ways we can sum S[0..m-1] coins to get sum n

def count(S, m, n):
    # If n is 0 then there is 1 solution (do not include any coin)
    if n == 0:
        return 1

    # If n is less than 0 then no solution exits
    if n < 0:
        return 0

    # If the are no coins and n is greater than 0, then no solution exits
    if m <= 0 and n >= 1:
        return 0

    # coun is sum of solutions (i) including S[m-1]
    # (ii) excluding S[m-1]
    return count(S, m, n - S[m - 1]) + count(S, m - 1, n)


# Initilazation program to test above function
arr = [1, 2, 3]
m = len(arr)
print(count(arr, m, 4))


# Dynamic Programming Python implementation of Coin change problem
def DP_count(S, m, n):
    # We need n+1 rows as the table is constructed in bottom up manner using the base
    # case 0 value case n = 0
    # m columns and n+1 rows
    table = [[0 for x in range(m)] for x in range(n + 1)]

    # fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # fill the rest of the table entries in bottom up manner
    for i in range(1, n + 1):  # money
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y
    return table[n][m - 1]


# Driver program to test DP count function
arr = [1, 2, 3]
m = len(arr)
n = 4
print("DP program: ", DP_count(arr, m, n))


# Simplified version of DP_count O(n)
def DP_count_simplified(S, m, n):
    # table[i] will be storing the number of solutions for value i
    # We need n+1 rows as the table is constructed in bottom manner using base case (n=0)
    # Initialize all table values as 0
    table = [0 for k in range(n + 1)]

    # base case
    table[0] = 1

    # Pick all coins one by one and update table[] values
    # after index greater than or equal to the value of the picked coin
    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]
    return table[n]


# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
x = DP_count_simplified(arr, m, n)
print(x)
