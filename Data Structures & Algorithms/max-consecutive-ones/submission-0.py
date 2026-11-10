class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for n in nums:
            print(n)
            if n == 1:
                count = count + 1

            else:
                count = 0
            
            if count > res:
                    res = count
        
        return res
        