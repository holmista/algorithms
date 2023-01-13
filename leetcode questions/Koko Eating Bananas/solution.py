import math

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        minHours = 1
        maxHours = max(piles)
        res = maxHours
        while minHours <= maxHours:
            m = (minHours + maxHours)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/m)
            if hours <= h:
                res = m
                maxHours = m-1
            else:
                minHours = m+1
        return res