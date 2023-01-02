class Solution:
    def isValid(self, s):
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                print(i, stack[-1])
                if len(stack) == 0:
                    return False
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return not len(stack)

sol = Solution()
print(sol.isValid("([)"))


# Input: s = "{[]}"
# Output: true