class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        self.tmp = ""

        def dfs(i):
            if i >= len(digits):
                res.append(self.tmp)
                return
            
            char = digitToChar[digits[i:i+1]]
            for j in range(len(char)):
                self.tmp = self.tmp + char[j]
                dfs(i+1)
                self.tmp = self.tmp[:-1]
        
        if not digits:
            return []
        dfs(0)
        return res
