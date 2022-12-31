class Solution:
    def romanToInt(self, s):
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        output = 0
        s = [*s]
        while len(s)>1:
            if ''.join(s[len(s)-2:len(s)]) in map:
                output += map[''.join(s[len(s)-2:len(s)])]
                s.pop()
                s.pop()
            else:
                output += map[s[-1]]
                s.pop()
        if len(s)==1:
            output += map[s[-1]]
        return output
        
sol = Solution()
print(sol.romanToInt("IV"))
        

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.


# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.