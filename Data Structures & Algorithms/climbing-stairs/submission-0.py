class Solution:
    def reccursion(self, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        a = self.reccursion(n - 1)
        b = self.reccursion(n - 2)

        return a + b

    def climbStairs(self, n: int) -> int:
        return self.reccursion(n)