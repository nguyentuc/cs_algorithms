# Given a string you need to print all possible strings that can be made by
# placing spaces (zero or one) between them

# Input:  str[] = "ABC"
# Output: ABC
#         AB C
#         A BC
#         A B C

# The idea is to use recursion and create a buffer that one by one contains all output string having
# space. Then, i keep updating the buffer in every recursive call
# If the length of the given string is n our updated string can have
# a maximum length of n+ (n-1). So the algorithm create a buffer size of 2n
# (no extra character for string termination)

# Leave 1st character as it is, starting from the 2nd character, we can either fill a space or a character.
# Thus one can write a recursive function like below

# Python program to print permutations of a given string with space

# Utility function
def toString(List):
    s = ""
    for x in List:
        if x == '&# 092;&# 048;':
            break
        s += x
    return s


# function recursively prints the string having space pattern
# i and j are indices in str[] and buff[] respectively

def printPatternUtil(string, buff, i, j, n):
    if i == n:
        buff[j] = '&# 092;&# 048;'
        print(toString(buff))
        return

    # either put the character
    buff[j] = string[i]
    printPatternUtil(string, buff, i + 1, j + 1, n)

    # Or put a space follow by next character
    buff[j] = ' '
    buff[j + 1] = string[i]
    printPatternUtil(string, buff, i + 1, j + 2, n)


# This function create buff[] to store individual output string an uses printPatternUtil() to
# print all permuations
def printPattern(string):
    n = len(string)
    # buffer to hodl the string containing spaces

    # 2n -1 characters and 1 string terminator
    buff = [0] * (2 * n)

    # copy the first character as it is, since it will be always at first position
    buff[0] = string[0]
    printPatternUtil(string, buff, 1, 1, n)


# Driver program
string = "ABCD"
printPattern(string)
