class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [0 for _ in range(len(nums)*2)]
        for i, n in enumerate(nums):
            arr[i] = n
            arr[i + len(nums)] = n
        
        return arr
        