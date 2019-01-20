def bubble_sort(l):
    n = len(l)

    for i in range(n):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    print(l)

arr = [8, 3, 9, 2, 1, 5]
bubble_sort(arr)
