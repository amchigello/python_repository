

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        pos = i-1
        while pos >= 0 and key < arr[pos]:
            arr[pos+1] = arr[pos]
            pos -= 1
        arr[pos+1] = key
    return arr
