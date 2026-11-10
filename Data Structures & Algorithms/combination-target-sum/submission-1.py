class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums) or sum(subset) > target:
                return
            if sum(subset) == target:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res







        # res = []
        # myset = set()

        # subset = []
        # def dfs(i):
        #     if sum(subset) > target or i >= len(nums):
        #         return
              
        #     if(sum(subset) == target):
        #         if tuple(subset) not in myset:
        #             myset.add(tuple(subset.copy()))
        #             res.append(subset.copy())
        #         return
            
        #     for j in range(i, len(nums)):
        #         subset.append(nums[i])
        #         dfs(j)
        #         subset.pop()
        
        # for k in range(len(nums)):
        #     dfs(k)
        # return res
        