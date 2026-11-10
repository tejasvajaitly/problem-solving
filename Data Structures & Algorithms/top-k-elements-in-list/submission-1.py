class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        bucket = [[] * i for i in range(len(nums) + 1)]

        for num, count in hashmap.items():
            bucket[count].append(num)
        
        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for v in bucket[i]:
                res.append(v)
                if len(res) == k:
                    return res
























        # hashmap = {}
        # for n in nums:
        #     if n in hashmap:
        #         hashmap[n] = hashmap[n] + 1
        #     else:
        #         hashmap[n] = 1

        # maxheap = []
        
        # for key, value in hashmap.items():
        #     heapq.heappush(maxheap, (-1*value, key))
        
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(maxheap)[1])
        
        # return res

            
        