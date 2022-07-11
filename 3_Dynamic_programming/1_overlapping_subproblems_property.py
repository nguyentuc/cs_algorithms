# Quy hoạch động là mô hình thuật toán có đặc điểm: cho một vấn đề với mức độ
# phức tạp cao, chia vấn đề đó thành các vấn đề nhỏ hơn và lưu kêt quả của
# các subproblems tránh việc phải tính toán lại
# 2 thuoc tính quan trọng
# Overlapping subproblems
# Optimal substructure

# tương tự chia để trị: các bài toán liên quan quy hoạch động cũng chia một solution thành các
# sub-problems và xử lý các subproblems đó.
# DP được dùng khi các solutions của một vấn đề được dùng đi dùng lại nhiều lần
# với kết quả được lưu ở bảng để tránh việc tính lại nhiều lần

# Khi thuật toán không có phần tái sử dụng thì không sử dụng DP
# Cài đặt chương trình đệ quy tính dãy trong chuỗi Fibonaci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# vì fib(2),.. được tái sử dụng lại khá nhiều do đó cần lưu giá trị để tránh việc phải tính lại
# có 2 cách: top down (memoization) và bottom up (tabulation)
# c1: top down: tao ra một mảng, khi cần đến giá trị của subproblems thì tìm trong
# mảng trước khi tính, nếu chưa có thì tính giá trị đó và lưu lại trọng mảng
# để tái sử dụng cho các lần sau

# Python program for Memoized version of nth Fibonacci number
def fibonacci(n, lookup):
    # base case
    if n == 0 or n == 1:
        lookup[n] = n
    # if the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fibonacci(n - 1, lookup) + fibonacci(n - 2, lookup)

    # return the value coressponding to that value of n
    return lookup[n]


# initialization for testing
def main():
    n = 34
    # declaration of lookup table
    lookup = [None] * 101
    print("Fibonacci number is ", fibonacci(n, lookup))


# main()

# c2: tabulation(bottom up)
# tao mot bang, tinh cac gi tri va luu truc tiep vao bang do
def fib_bottomup(n):
    # array declaration
    f = [0] * (n + 1)
    # base case
    f[1] = 1
    # calculating the fibonacci and storing the values
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


# initlization for test
n = 34
print("Fibobacci bottom up:", fib_bottomup(34))

# trong phương pháp top down memorization thì tất cả các phần tử trong bảng
# không nhất thiết phải lưu trữ vì trong một số case không thể nào lưu
# được tất cả các phần từ

# Có nhiều phương pháp tối ưu dựa trên 2 hướng giải quyết này
