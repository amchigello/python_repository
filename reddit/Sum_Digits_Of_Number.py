
result = 0


def sum_of_digits(n):
    global result
    result = n[0] + result
    if len(n) != 1:
        n = n[1:]
        result = sum_of_digits(n)
        return result
    else:
        return result


if __name__ == '__main__':
    x = 4367
    xlist = [int(x) for x in str(x)]
    print(sum_of_digits(xlist))
