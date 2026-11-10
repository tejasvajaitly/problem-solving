class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        
        def dfs(r, c, curr):
            print(curr)
            if curr == word:
                return True
            if len(curr) > len(word):
                return False
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit:
                return False
            

            visit.add((r, c))
            curr = curr +  board[r][c]
            res = dfs(r+1, c, curr) or dfs(r, c+1, curr) or dfs(r-1, c, curr) or dfs(r, c-1, curr)
            visit.remove((r, c))
            curr = curr[:-1]
            return res
        
        res = False
        for r in range(ROWS):
            for c in range(COLS):
                res = res or dfs(r, c, "")
        
        return res
            
            
             
            

        