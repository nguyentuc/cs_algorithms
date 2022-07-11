# We can multiple by 7 using bitwise operator.
# First left shift the number by 3 bits (get 8n) then subtract the
# origin number from the shifted number and return the differences
# between the origin and the the shfted number (8n - n)

# Python program to multiply any positive number to 7
def multiplyBySeven(n):
    return ((n << 3) - n)


# Driver code
n = 4
print(multiplyBySeven(n))

# Time complexity: O(1)
# Space conplexity: O(1)