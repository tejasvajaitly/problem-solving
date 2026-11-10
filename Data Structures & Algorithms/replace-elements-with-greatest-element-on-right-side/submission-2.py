class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        prev = 0

        for i in range(len(arr) - 1, -1, -1):
            if i + 1 < len(arr):
                tmp = arr[i]
                arr[i] = max(prev, arr[i + 1])
                prev = tmp

        arr[-1] = -1

        return arr


        # tmp = [0] * len(arr)

        # for i in range(len(arr) - 1, -1, -1):
        #     if (i + 1) < len(arr):
        #         tmp[i] = max(tmp[i+1], arr[i+1])
        #     else:
        #         tmp[i] = arr[i]
        
        # tmp[-1] = -1

        # return tmp
        





        # l = 0
        # while l < len(arr):
        #     g = 0
        #     for i in range(l + 1, len(arr)):
        #         g = max(g, arr[i])
            
        #     arr[l] = g
        #     l = l + 1
        
        # arr[len(arr) - 1] = -1

        # return arr
        