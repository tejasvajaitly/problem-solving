class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                nums[r] = None
                r = r - 1
            else:
                l = l + 1
        
        return l