def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    found = False
    while not found:
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1 

print(twoSum([2,7,11,15], 9))