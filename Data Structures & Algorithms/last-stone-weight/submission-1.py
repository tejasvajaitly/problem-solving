class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1

            if x == y:
                continue
            
            heapq.heappush(stones, (y - x) * -1)
        
        return stones[0] * -1 if stones else 0
        