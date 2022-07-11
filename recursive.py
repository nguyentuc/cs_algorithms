class Fibonacci(object):
    @staticmethod
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return Fibonacci.fibonacci(n - 1) + Fibonacci.fibonacci(n - 2)

    @staticmethod
    def main(self, n):
        n = 10
        print("Fibonacci for the sequence of %d elements:", n)
        for i in range(n):
            print(Fibonacci.fibonacci(i))


f = Fibonacci()
f.main(f, 100)

# su dung static method ham khong can dung self vi khi goi tu class thi object se duoc tu dong khoi tao va pass vao func
# tuy nhien voi ham khong phai static method khi co self muon goi lai can phai khoi tao mot object cho class
