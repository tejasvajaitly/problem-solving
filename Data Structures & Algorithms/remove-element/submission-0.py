class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []

        for i, n in enumerate(nums):
            if(n == val):
                nums[i] = None
        
        for i, n in enumerate(nums):
            if n != None:
                res.append(nums[i])

        for i, n in enumerate(res):
            nums[i] = n
        
        return len(res)