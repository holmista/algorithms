class Solution:
    def topKFrequent(self, nums, k):
        freqDict = {}
        for i in nums:
            if i in freqDict:
                freqDict[i] += 1
            else:
                freqDict[i] = 1
        freqArr = [[] for i in range(len(nums)+1)]
        for i in freqDict:
            freqArr[freqDict[i]].append(i)
        res = []
        count = 0
        for i in range(len(freqArr)-1, -1, -1):
            if count == k:
                break
            if len(freqArr[i]) > 0:
                for j in freqArr[i]:
                    res.append(j)
                    count += 1
                    if count == k:
                        break
        return res
        # for i in range(len(nums)+1):
        #     if
        

sol = Solution()
print(sol.topKFrequent([1,1,1], 1))
# Input: nums = [1,1,1,2,2,3], k = 2
# {1:3, 2:2, 3:3}
# ['-inf', '-inf']
# Output: [1,2]

# 8, 3, 2 - 3
# 10,3, 2 - 3
# 12,3, 2 - 4
# 10,4, 2 - 3
# 12,4, 2 - 4
# 14,4, 2 - 