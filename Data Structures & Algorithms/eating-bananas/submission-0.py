class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float('inf')

        def calculate(mid):
            t = 0
            for p in piles:
                t = math.ceil(p/mid) + t
            return t

        while l <= r:
           
            mid = (l+r) // 2
            hours = calculate(mid)
            print(mid, hours)
            if hours > h:
                l = mid + 1
            elif hours <= h:
                res = min(res, mid)
                r = mid - 1

        
        return res

        