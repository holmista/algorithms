import math

class Solution:
    def evalRPN(self, tokens) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for i in tokens:
            if i not in ['*', '/', '+', '-']:
                stack.append(i)
            else:
                result = None
                if i == '/':
                    expression = f'{stack[-2]} {i} {stack[-1]}'
                    result = eval(expression)
                    if result > 0:
                        result = math.floor(result)
                    else:
                        result = math.ceil(result)
                else:
                    expression = f'{stack[-2]} {i} {stack[-1]}'
                    result = eval(expression)
                stack.pop()
                stack.pop()
                stack.append(result)
        return stack[0]

        

sol = Solution()
print(sol.evalRPN(["18"]))

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

#  [4, 13]
#  [+, /]
#  result = 5
#  13 / result and make dis value to result
#   4+result and make dis result
#   
# 
# 
# 
# 
# 
print(math.floor(6/-132))
