class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [[] for _ in range(3)]

        for c in nums:
            if c == 0:
                bucket[0].append(c)
            elif c == 1:
                bucket[1].append(c)
            else:
                bucket[2].append(c)
        
        index = 0
        for b in bucket:
            for c in b:
                nums[index] = c
                index = index + 1

        return nums
                

            


        