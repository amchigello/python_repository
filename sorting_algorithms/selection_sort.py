def selection_sort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i + 1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j

        l[i], l[min_idx] = l[min_idx], l[i]
    print(l)


arr = [1, 11, 1, 8, 23, 2, 6, 3, 8]

selection_sort(arr)
