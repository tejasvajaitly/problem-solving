class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = 0
        while l < len(arr):
            g = 0
            for i in range(l + 1, len(arr)):
                g = max(g, arr[i])
            
            arr[l] = g
            l = l + 1
        
        arr[len(arr) - 1] = -1

        return arr
        