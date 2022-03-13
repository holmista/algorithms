class Solution:
    def __init__(self, cache={}):
        self.cache = cache
    def fib(self, n: int) -> int:
        if n==0: return 0
        if n==1:return 1
        if n in self.cache: return self.cache[n]
        self.cache[n] = self.fib(n-1)+self.fib(n-2)
        return self.cache[n]