class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                diff = 0 - nums[i] - nums[l]
                if nums[r] == diff:
                    arr = [nums[i], nums[l], nums[r]]
                    res.append(arr)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[r] > diff:
                    r -= 1
                else:
                    l += 1
        
        return res



                
        