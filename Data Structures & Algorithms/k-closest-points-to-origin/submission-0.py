class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashmap = {}
        minheap = []
        heapq.heapify(minheap)
        res = []

        def cal(x, y):
            a = pow(x-y, 2)
            b = pow(x+y, 2)
            return math.sqrt(a+b)

        for x, y in points:
            dis = cal(x, y)
            if dis in hashmap:
                hashmap[dis].append([x, y])
            else:
                hashmap[dis] = [[x, y]]
            
            heapq.heappush(minheap, dis)
        
        for _ in range(k):
            dis = heapq.heappop(minheap)
            coord = hashmap[dis].pop()
            res.append(coord)
        
        return res



        