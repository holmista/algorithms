def sumOfNestedArray(arr):
    if len(arr) == 0:
        return 0
    total = 0
    for i in arr:
        if type(i) == int:
            total += i
        else:
            total += sumOfNestedArray(i)
    return total


print(sumOfNestedArray([[[[[[10, 10]]]], [10, 10, [10, 10]]], 10, []]))
