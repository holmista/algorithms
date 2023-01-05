class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                print(nums[i], nums[i-1])
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))