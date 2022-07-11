# Given weights and values of n items, put these items in a knapsack
# capacity W to get the maximum total value in the knapsack
# In other words, given two integer arrays val[0..n-1] and wt[0..n-1]
# which represent values and weights associated with n items respectively.
# Also given an integer W which represents knapsack capacity, find out the
# maximum value subset of val[] such that sum of the weights of this subset
# is smaller than or equal to W
# Mot mon chi chon toi da 1 lan

# Method 1: Recursion
# Xem tất cả các subset items và tính tổng trọng số và giá trị trên tất cả
# subset. Kiểm tra từ các subset có tổng trọng số nhỏ hơn W từ đó lấy ra các
# subset có giá trị lớn nhất

# Two case can be consider:
# Case 1: The item is included in the optimal subset.
# Case 2: The item is not included in the optimal set.

# Therefore, the maximum value that can be obtained from ‘n’
# items is the max of the following two values
# Maximum value obtained by n-1 items and W weight (excluding nth item).
# Value of nth item plus maximum value obtained by n-1 items and W minus the weight of the nth item (including nth item).
# If the weight of nth item is greater than W, then nth item cannot be include and
# case 1 is the only possibility

# A naive recursive Python implement of 0-1 Knapsack problem
# return the maximum value that can be put in a knapsack of cappacity W

def knapSack(W, wt, val, n):
    # base case
    if n == 0 or W == 0:
        return 0

    # if weight of the nth item is more than Knapsack of capacity W, then this item
    # cannnot be included in the optimal solution
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)

    # return the maximum of two cases
    # (1) nth item includes
    # (2) not included
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1), knapSack(W, wt, val, n - 1))


# driver code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
