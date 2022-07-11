# Karatsuba Multiplication for fast multiple long intergers
# function to multiple 2 numbers in a more efficient manner than the
# grade school algorithms

def karatsuba(x, y):
    if len(str(x)) <= 5 or len(str(y)) <= 5:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2

        a = x // 10 ** nby2
        b = x % 10 ** nby2
        c = y // 10 ** nby2
        d = y % 10 ** nby2

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
        result = ac * 10 ** (2 * nby2) + (ad_plus_bc * 10 ** nby2) + bd

        return result


from math import ceil, floor


def karatsuba2(X, Y):
    # Base case
    if X < 10 and Y < 10:
        return X * Y

    # determine the size of X and Y
    size = max(len(str(X)), len(str(Y)))

    # Split X and Y
    n = ceil(size // 2)
    p = 10 ** n
    a = floor(X // p)
    b = X % p
    c = floor(Y // p)
    d = Y % p

    # Recur until base case
    ac = karatsuba2(a, c)
    bd = karatsuba2(b, d)
    e = karatsuba2(a + b, c + d) - ac - bd

    # return the equation
    return int(10 ** (2 * n) * ac + (10 ** n) * e + bd)


print("Result: ", karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                            2718281828459045235360287471352662497757247093699959574966967627))


# naive implementation of multiple two large number
def multiplication(X, Y):
    # convert numbers into string
    x = str(X)
    y = str(Y)
    result = 0
    # looping over y
    for i in range(len(y)):
        carry = 0
        inter_res = ""
        # looping over x
        for j in range(len(x) - 1, -1, -1):
            # intermediate multiplication of each digit and addition of carry
            num = int(y[i]) * int(x[j]) + carry
            # if intermediate multiplication is of two digits and j>0
            #   then second digit is appended to intermediate result
            #   and first digit is stored as carry
            if num > 9 and j > 0:
                inter_res = str(num % 10) + inter_res
                carry = num // 10
            # else the digit is append to intermediate result
            # And assign carry as zero
            else:
                inter_res = str(num) + inter_res
                carry = 0
        result *= 10
        result += int(inter_res)
    return result


print("Result: ", multiplication(30, 70))
