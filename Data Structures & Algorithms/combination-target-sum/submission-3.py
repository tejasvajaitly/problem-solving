class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(set, startIndex):
            if sum(set) == target:
                res.append(set.copy())
                return
            if sum(set) > target:
                return

            for i in range(startIndex,len(nums)):
                set.append(nums[i])
                dfs(set, i)
                set.pop()

        dfs([], 0)
        return res        