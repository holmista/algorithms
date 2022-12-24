class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        for i in range(len(strs)):
            sortedStr = ''.join(sorted(strs[i]))
            if sortedStr in dict:
                dict[sortedStr].append(strs[i])
            else:
                dict[sortedStr] = [strs[i]]
        result = []
        for i in dict:
            result.append(dict[i])
        return result
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

arr = ["eat","ate","tan","tae","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(arr))

