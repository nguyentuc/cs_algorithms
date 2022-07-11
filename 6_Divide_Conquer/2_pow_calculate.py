# given x and n return x^n
def power(x, y):
    if y == 0:
        return 1
    elif int(y % 2) == 0:
        return power(x, int(y / 2)) * power(x, int(y / 2))
    else:
        return x * power(x, int(y / 2)) * power(x, int(y / 2))


# Driver Code
x = 2
y = 3
print(power(x, y))


# time complexity: O(n)
# space complixity: O(1)

# optimized verion to complexity O(logn) by calculating power(x, y/2) only
# once and sotring it
def optimized_power(x, y):
    if y == 0:
        return 1
    temp = power(x, int(y / 2))
    print(temp)
    if y % 2 == 0:
        return temp * temp
    else:
        if y > 0:
            return x * temp * temp
        else:
            return (temp * temp) / x


# Driver Code
x, y = 2, 6
print('%.6f' % (optimized_power(x, y)))
