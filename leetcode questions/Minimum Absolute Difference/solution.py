class Solution:
    def minimumAbsDifference(self, arr):
        # initializing array to return
        pairs = []
        # sorting the array
        arr.sort()
        # calculating the differences
        differences = []
        for i in range(1,len(arr)):
            difference = arr[i]-arr[i-1]
            differences.append(difference)
        # getting minimum difference
        minDifference = min(differences)
        # iterating over differences array
        for j in range(len(differences)):
            # checking for minimum difference
            if differences[j]==minDifference:
                # mapping index of minimum difference to corresponding numbers in arr and pushing them to pairs array 
                pairs.append([arr[j], arr[j+1]])
        return pairs

s1 = Solution()
print(s1.minimumAbsDifference([4,2,1,3]))