# Find square root of a number using binary search algorithm
# Given a positive number, find the square root of it
# If a number is not a perfect square, then return the floor of its square


# A naive solution is to consider all positive numbers starting from 1 and
# find the first number i for which i^2 is greater than given number x
# then i - 1 would be the floor of the square root of x

def sqrt(x):
    i = 1
    while i * i <= x:
        i = i + 1
    return i - 1


if __name__ == '__main__':
    for i in range(17):
        print(f"sqrt({i}) = {sqrt(i)}")


# time complexity of above function is O(sqrt(n)) and doesn't need extra space
# we can improve the time complexity into O(log(x)) with the help of
# binary search algorithm
def improve_sqrt(x):
    if x <= 3:
        return 1
    if x == 4:
        return 2
    # to store floor of sqrt(x)
    result = 0
    # the square root of x cannot be more than x/2 for x >= 4
    start = 1
    end = x // 2
    while start <= end:
        # find the middle element
        mid = (start + end) // 2
        sqr = mid * mid

        # return mid if x is a perfect square
        if sqr == x:
            return x

        # if mid* mid less than x
        elif sqr < x:
            # discard left search peace
            start = mid + 1
            # update result since we need a floor
            result = mid
        else:
            end = mid - 1
    return result


print("Improve sqrt")
if __name__ == "__main__":
    for i in range(17):
        print(f"sqrt({i}) = {sqrt(i)}")
