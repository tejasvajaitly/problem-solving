class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1

        res = 0

        while s < len(prices):
            if  prices[s] < prices[b]:
                # tmp = s
                # b = s
                # s = tmp + 1
                b = s

            
            
            res = max(res, prices[s] - prices[b])

            s = s + 1
        
        return res















        # res = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         res = max(res, prices[j] - prices[i])
        
        # return res


        