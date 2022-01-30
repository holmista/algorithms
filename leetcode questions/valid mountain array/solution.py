class Solution:
    def validMountainArray(self, arr):
        if len(arr)<=2:return False
        tip = arr[0]
        tipReached=False
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:return False
            if arr[i+1]>arr[i]:
                tip=arr[i+1]
                if tipReached==False:
                    continue
                else:return False
            else:
                tipReached=True
        if arr.index(max(arr)) in [0, len(arr)-1]:return False
        return True