def findTop3Max(arr):
    first, second, third = float("-inf"), float("-inf"), float("-inf")
    for i in arr:
        if i > first:
            second, third = first, second
            first = i
        elif i > second:
            third = second
            second = i
        elif i > third:
            third = i
    return [first, second, third]

print(findTop3Max([1, 2, -2, 5, 9, 4, 7]))