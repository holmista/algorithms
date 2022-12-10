def partition(arr, lo, high):
    pivot = arr[lo]
    i = lo
    j = high
    while i <= j:
        while arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    return j

# arr = [10, 5, 8, 9, 3, 6, 15, 12, 16]
def quicksort(arr, lo, high):
    if(lo<high):
        j = partition(arr, lo, high)
        print(j)
        quicksort(arr, lo, j)
        quicksort(arr, j+1, high)
    return arr

print(quicksort([10, 5, 8, 9, 3, 6, 15, 12, 16],0, 8))

# print(partition([10, 5, 8, 9, 3, 6, 15, 12, 16], 0, 8))

# [6, 5, 8, 9, 3, 10, 15, 12, 16] - 10, 0, 9; [10, 16, 8, 12, 15, 6, 3, 9, 5]

