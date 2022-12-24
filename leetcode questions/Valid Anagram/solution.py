class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in t:
            if i in dict:
                dict[i] -= 1
                if dict[i] < 0:
                    return False
            else:
                return False
        return True

sol = Solution()
print(sol.isAnagram('carrr', 'arcrk'))
# Input: s = "anagram", t = "nagaram"
# Output: true