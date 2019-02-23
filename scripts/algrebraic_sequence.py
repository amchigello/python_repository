
def geometric_progression(a, r, n):
    x = [a*(r**i) for i in range(1, n+1)]
    print(x)


def arithmetic_progression(a, d, n):
    x = [a+(i-1)*d for i in range(1, n+1)]
    print(x)


geometric_progression(1, 2, 10)
arithmetic_progression(1, 2, 10)
