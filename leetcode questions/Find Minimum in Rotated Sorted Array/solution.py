class Solution:
    def findMin(self, nums):
        l = 0
        r = len(nums)-1
        while r-l>1:
            m = (l+r) // 2
            if nums[m] > nums[r] and nums[m] > nums[l]:
                l = m+1
            else:
                r = m
            print(l, r, m)
        return min(nums[l], nums[r])