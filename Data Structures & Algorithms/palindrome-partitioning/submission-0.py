class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(substr):
            print(substr)
            arr = list(substr)
            l, r = 0, len(arr) - 1
            
            while l < r:
                if arr[l] != arr[r]:
                    return False
                l, r = l + 1, r - 1
            
            return True
        
        res = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res

            

        