class Solution:
    def productExceptSelf(self, nums):
        prefixArr, postfixArr = [1], [1]
        for i in nums:
            prefixArr.append(prefixArr[-1]*i)
        for i in range(len(nums)-1, -1, -1):
            postfixArr.insert(0, postfixArr[0]*nums[i])
        print(prefixArr, postfixArr)
        res = []
        for i in range(len(prefixArr)):
            res.append(prefixArr[i]*postfixArr[i+1])
            if i+1==len(nums):
                return res
    def productExceptSelfV2(self, nums):
        pass


sol = Solution()
print(sol.productExceptSelf([-1,1,0,-3,3]))