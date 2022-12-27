class Solution:
    def longestConsecutive(self, nums):
        sett = set(nums)
        count = 0
        for i in nums:
            if i-1 in sett:
                continue
            else:
                localCount = 1
                currentNum = i
                while (currentNum+1 in sett):
                    localCount += 1
                    currentNum += 1
                if localCount > count:
                    count = localCount
        return count


sol = Solution()
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

