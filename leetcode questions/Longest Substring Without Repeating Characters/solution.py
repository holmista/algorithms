class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        current_len = 0
        dict = {}
        while r < len(s):
            if s[r] in dict:
                del dict[s[l]]
                l+=1
                current_len -= 1
            else:
                dict[s[r]] = r
                current_len+=1
                r+=1
                if current_len>max_len:
                    max_len = current_len
        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring("dvdf"))