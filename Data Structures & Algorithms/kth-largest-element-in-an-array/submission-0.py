class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
        heapq.heapify(nums)
        res = 0
        for _ in range(k):
            res = heapq.heappop(nums)
        
        return res * -1




        