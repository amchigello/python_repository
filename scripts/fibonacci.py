

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


def fib(n):
    first, second = 0, 1
    fib_series = [first, second]
    for i in range(2, n):
        next_num = first + second
        fib_series.append(next_num)
        first, second = second, next_num
    return fib_series


print([Fibonacci(i) for i in range(10)])
print(fib(10))
