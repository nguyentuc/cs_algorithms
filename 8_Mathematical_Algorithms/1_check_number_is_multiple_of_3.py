# https://www.geeksforgeeks.org/write-an-efficient-method-to-check-if-a-number-is-multiple-of-3/

# Python program to check if n is a multiple of 3
# function to check if n is a multiple of 3

# Algorithm: isMutlipleOf3(n)
# 1) Make n positive if n is negative.
# 2) If number is 0 then return 1
# 3) If number is 1 then return 0
# 4) Initialize: odd_count = 0, even_count = 0
# 5) Loop while n != 0
#     a) If rightmost bit is set then increment odd count.
#     b) Right-shift n by 1 bit
#     c) If rightmost bit is set then increment even count.
#     d) Right-shift n by 1 bit
# 6) return isMutlipleOf3(odd_count - even_count)

def isMultipleOf3(n):
    odd_count = 0
    even_count = 0
    # make no positive if +n is multiple of 3
    # then is -n. We are doing this to avoid
    # stack overflow in recursion
    if n < 0:
        n = -n
    if n == 0:
        return 1
    if n == 1:
        return 0
    while n:
        # if odd bit is set then increment odd counter
        # &: thu hien phep tính and dưới dạng bit
        if n & 1:
            odd_count += 1
        # If even bits is set then increment even counter
        if n & 2:
            even_count += 1
        n = n >> 2  # bieu dien duoi dang bit nhi phan 8 chu so (thay the 2 so 0 vao ben trai)
    return isMultipleOf3(abs(odd_count - even_count))


# Program to test function isMultipleOf3
num = 24
if (isMultipleOf3(num)):
    print(num, 'is multiple of 3')
else:
    print(num, 'is not a multiple of 3')
