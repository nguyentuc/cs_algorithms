# The time complexity of 8_Edit_distance.py is exponential, in worst case, we
# may end up doing with o(3^m) operations
# the worst case when none of characters of two string match.
# edit distance có 2 thuộc tính của thuật toán quy hoạch động là
# Overlapping problem và Optimal substructure
# A Dynamic Programming based Python program for edit distance

def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    #  fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # if first string is empty, only option is to insert all characters of second string
            if i == 0:
                dp[i][j] = j

            # If second string is empty, only option is to remove all characters of second
            # string
            elif j == 0:
                dp[i][j] = i

            # If last characters are sane, ignore last char and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all posibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace
    return dp[m][n]


# Initilization
str1 = "sunday"
str2 = "saturday"

print(editDistDP(str1, str2, len(str1), len(str2)))
