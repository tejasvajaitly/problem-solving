class Solution:
    def reccursion(self, n, cache):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if cache[n] != -1:
            return cache[n]
        cache[n] = self.reccursion(n - 1, cache) + self.reccursion(n - 2, cache)
        return cache[n]

    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)
        return self.reccursion(n, cache)