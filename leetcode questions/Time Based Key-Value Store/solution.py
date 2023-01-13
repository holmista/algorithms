class Node:
    def __init__(self, val, timestamp):
        self.val = val
        self.timestamp = timestamp

class TimeMap:
    def __init__(self):
        self.dict = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append(Node(value, timestamp))
        else:
            self.dict[key] = [Node(value, timestamp)]
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.dict:
            return ''
        if timestamp<self.dict[key][0].timestamp:
            return ''
        search = self._binarySearch(self.dict[key], timestamp)
        print(search)
        if search[1] == True:
            return self.dict[key][search[0]].val
        if self.dict[key][search[0]].timestamp < timestamp:
            return self.dict[key][search[0]].val
        return self.dict[key][search[0]-1].val
    def _binarySearch(self, arr, elemToFind):
        left = 0
        right = len(arr)
        mid = None
        while right > left:
            mid = (left + right) // 2
            if arr[mid].timestamp == elemToFind:
                return [mid, True]
            elif arr[mid].timestamp > elemToFind:
                right = mid
            else:
                left = mid + 1
        return [mid, False] 
        
        

# [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo","bar",1)
print(obj.get("foo",1))
print(obj.get("foo",3))
obj.set("foo","bar2",4)
print(obj.get("foo",4))
print(obj.dict)
print(obj.get("foo",5))
# param_2 = obj.get(key,timestamp)