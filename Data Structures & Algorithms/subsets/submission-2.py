class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def graph(set, level):
            if level >= len(nums):
                res.append(set.copy())
                return

            graph(set, level + 1)
            set.append(nums[level])
            graph(set, level + 1)
            set.pop()


        graph([], 0)
        return res