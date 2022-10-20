def bubble_sort(arr):
    for i in range(len(arr)):
        for k in range(len(arr)-1-i):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr

print(bubble_sort([1, 4, 2, 7, 3, 9]))