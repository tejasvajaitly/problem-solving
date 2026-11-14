class Solution:
    def climbStairs(self, n: int) -> int:
        hash = {}

        def rec(s):
            if s in hash:
                return hash[s]
            if s == 0:
                return 1
            if s == 1:
                return 1
            

            climbOne = rec(s-1)
            climbTwo = rec(s - 2)

            tmp = climbOne + climbTwo
            hash[s] = tmp
            return tmp

        return rec(n)

        