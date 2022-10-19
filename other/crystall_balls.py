from math import ceil
from re import S


def crystal_balls(arr):
    step = round(len(arr)**0.5)
    for i in range(0, len(arr), step):
        if arr[i] == 1:
            for k in range(i-step, i):
                print('oit', k)
                if arr[k] == 1:
                    return k
                
print(crystal_balls([0, 0, 0, 0, 1, 1, 1, 1, 1]))

