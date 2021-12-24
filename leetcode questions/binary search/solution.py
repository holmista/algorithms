class Solution:
    def search(self, nums, target):
        if len(nums)==0: return -1
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (r+l)//2
            if nums[m]==target: return m
            elif nums[m]<target: l=m+1
            else: r=m-1
        return -1