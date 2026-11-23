class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:




        def doesItWork(rate):
            totalHoursToEat = 0
            for i, p in enumerate(piles):
                hoursToEatPile = p // rate
                remainder = p % rate
                if remainder != 0:
                    hoursToEatPile = hoursToEatPile + 1
                
                totalHoursToEat = totalHoursToEat + hoursToEatPile

            
            if totalHoursToEat <= h:
                return True
            else:
                return False


        minRate = 1
        maxRate = max(piles)
        result = maxRate

        while minRate <= maxRate:
            midRate = (minRate + maxRate) // 2
            if doesItWork(midRate):
                result = min(result, midRate)
                maxRate = midRate - 1
            else:
                minRate = midRate + 1
        
        return result
                







        