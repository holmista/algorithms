class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        maxAmount = 0
        while l < r:
            amount = min(height[l], height[r]) * (r-l)
            if amount > maxAmount:
                maxAmount = amount
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1 
        return maxAmount

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))