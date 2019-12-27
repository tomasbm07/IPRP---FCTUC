memo = [0 for i in range(1000)]


def Fibonacci(n):
    if n <= 1:
        return 1
    else:
        if memo[n] != 0:
            return memo[n]
        a = Fibonacci(n - 1)
        b = Fibonacci(n - 2)
        memo[n-1] = a
        memo[n-2] = b
        return a + b


print(Fibonacci(200))
