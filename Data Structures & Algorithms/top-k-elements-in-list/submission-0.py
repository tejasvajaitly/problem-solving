class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] = hashmap[n] + 1
            else:
                hashmap[n] = 1

        maxheap = []
        
        for key, value in hashmap.items():
            heapq.heappush(maxheap, (-1*value, key))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(maxheap)[1])
        
        return res

            
        