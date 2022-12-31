class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []
        stack.append({'day':0, 'temp':temperatures[0]})
        for i in range(1, len(temperatures)):
            stack.append({'day':i, 'temp':temperatures[i]})
            while len(stack)>1 and stack[-1]['temp'] > stack[-2]['temp']:
                diff = stack[-1]['day'] - stack[-2]['day']
                answer[stack[-2]['day']] = diff
                stack.pop(-2)
        return answer

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# [{day:0, temp:73}, {day:1, temp:74}]
# [1, 1,4,2,1,1, 0, 0]
# [{day:6, temp:76}, {day:7, temp:73}]

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Input: temperatures = [30,60,90]
# Output: [1,1,0]