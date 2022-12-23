class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)

sol = Solution()
print(sol.containsDuplicate([1,2,3,4,5, 5]))