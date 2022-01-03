class Solution:
    def maxSubArray(self, nums):
        currentSum = nums[0]
        maxSum = currentSum
        for i in range(1, len(nums)):
            currentSum += nums[i]
            if nums[i] > currentSum:
                currentSum = nums[i]
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum
