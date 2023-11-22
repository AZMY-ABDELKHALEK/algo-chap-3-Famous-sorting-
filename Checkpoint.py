def insertion_sort(arr):
2    for i in range(1, len(arr)):
3        key = arr[i]
4        j = i - 1
5        while j >= 0 and key < arr[j]:
6            arr[j + 1] = arr[j]
7            j -= 1
8        arr[j + 1] = key
9    return arr
