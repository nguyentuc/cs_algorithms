# Given a string A of digits, find the length of the longest substring of A
# such that the length of the substring is 2k digits and sum of left k digits is
# equal to the sum of the right k digits

# example:
# Input: str = "1538023"
# Output: 4
# The longest substring with same first and second half sum is "5380"

# Simple solution: O(n^3)
# A simple solution is to check every substring of even length. The following is
# the implementation of simple approach

def simple_findLength(str):
    n = len(str)
    maxlen = 0  # Inititalize result

    # choose starting point of every substring
    for i in range(0, n):
        # choose ending point of even length substring
        for j in range(i + 1, n, 2):
            # find length of current substring
            length = j - i + 1
            # calculating left and right sum for current substring
            leftsum = 0
            rightsum = 0
            for k in range(0, int(length / 2)):
                leftsum += (int(str[i + k]) - int('0'))
                rightsum += (int(str[i + k + int(length / 2)]) - int('0'))

            # Update result if needed
            if leftsum == rightsum and maxlen < length:
                maxlen = length
    return maxlen


# Driver program to test above function
str = "1538023"
print("Length of the substring is", simple_findLength(str))


# Dynamic programming O(n^2) and O(n^2) extra space
def DP_findLength(string):
    n = len(string)
    maxlen = 0  # Initialize result

    # A 2D table where sum[i][j] stores sum of digits from str[i] to str[j]
    # Only filled entries are the entries where j >i
    Sum = [[0 for x in range(n)] for y in range(n)]

    # Fill the diagonal values for substrings of length 1
    for i in range(0, n):
        Sum[i][i] = int(string[i])

    # Fill entries for substrings of length 2 to n
    for length in range(2, n + 1):
        # pick i and j for current substring
        for i in range(0, n - length + 1):
            j = i + length - 1
            k = length // 2
            # calculating the value of sum[i][j]
            Sum[i][j] = (Sum[i][j - k] + Sum[j - k + 1][j])

            # Update result if len is even,leff and right sums are same and
            # length is more than maxlen
            if (length % 2 == 0 and Sum[i][j - k] == Sum[(j - k + 1)][j]) and length > maxlen:
                maxlen = length

    return maxlen


# Driver code
if __name__ == '__main__':
    string = '153803'
    print("Length of the substring is", DP_findLength(string))


# The idea is to use a single dimensional array to store culmulative sum
# O(n^2) time and O(n) extra space solution
def DP_optimize_findLength(string, n):
    # to store cumulative sum from first digit to nth digit
    Sum = [0] * (n + 1)

    # Store cumulative sum of digits from first to last digit
    for i in range(1, n + 1):
        Sum[i] = (Sum[i - 1] + int(string[i - 1]))

    ans = 0  # Initialize result
    # consider all even length substrings one by one
    for length in range(2, n + 1, 2):
        for i in range(0, n - length + 1):
            j = i + length - 1
            # sum of first and second half is same than update ans
            if Sum[i + length // 2] - Sum[i] == Sum[i + length] - Sum[i + length // 2]:
                ans = max(ans, length)
    return ans


# Driver code
if __name__ == "__main__":
    string = "123123"
    print("Length of the substring is", DP_optimize_findLength(string, len(string)))


# A O(n2) time and O(1) extra space solution
def more_optimize_findlength(st, n):
    # to store cumulative total from first digit to nth digit
    total = [0] * (n + 1)
    # store cumulative total of digits from first to last digit
    for i in range(1, n + 1):
        # convert chars to int
        total[i] = (total[i - 1] + int(st[i - 1]) - int('0'))

    ans = 0
    # consider all even length substring one by one
    l = 2
    while l <= n:
        for i in range(n - l + 1):
            j = i + l - 1
            # total of first and second half is same than update ans
            if total[i + int(l / 2)] - total[i] == total[i + l] - total[i + int(l / 2)]:
                ans = max(ans, l)
        l = l + 2
    return ans


# Driver Code
st = "123123"
print("Length of the substring is",
      more_optimize_findlength(st, len(st)))
