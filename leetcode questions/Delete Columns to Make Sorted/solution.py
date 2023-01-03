class Solution:
    def minDeletionSize(self, strs):
        toDelete = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if ord(strs[j][i]) > ord(strs[j+1][i]):
                    toDelete += 1
                    break
        return toDelete