class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)
        print(cache)
        def reccursion(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if cache[n] != -1:
                return cache[n]
            cache[n] = reccursion(n - 1) + reccursion(n - 2)
            return cache[n]

        return reccursion(n)