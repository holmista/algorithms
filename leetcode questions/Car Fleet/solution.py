class Solution:
    def carFleet(self, target: int, position, speed):
        times = []
        for i in range(len(position)):
            remainingDistance = target - position[i]
            timeToArrive = remainingDistance / speed[i]
            times.append({'timeToArrive':timeToArrive, 'position':position[i]})
        sortedTimes = sorted(times, key=lambda x:x['position'])
        fleets = 1
        max = sortedTimes[-1]['timeToArrive']
        for i in range(len(sortedTimes)-1, -1, -1):
            if sortedTimes[i]['timeToArrive'] > max:
                fleets+=1
                max = sortedTimes[i]['timeToArrive']
        return fleets

sol = Solution()
print(sol.carFleet(target = 10, position = [3], speed = [3]))