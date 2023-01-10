class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        last = self.right.prev
        last.next = node
        node.prev = last
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            toRemove = self.left.next
            self.remove(toRemove)
            del self.cache[toRemove.key]

cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
cache.get(1)
cache.put(3,3)
print(cache.cache)
print(cache.get(2))

