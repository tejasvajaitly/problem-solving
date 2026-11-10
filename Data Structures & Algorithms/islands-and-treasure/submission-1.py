class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addDist(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == -1:
                return
            q.append((r, c))
            visit.add((r, c))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))

        dist = 0
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addDist(r + 1, c)
                addDist(r - 1, c)
                addDist(r, c + 1)
                addDist(r, c - 1)
            dist = dist + 1
        






























        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # INF = 2147483647

        # def bfs(r, c):
        #     q = deque()
        #     q.append((r, c))
        #     level = 0
        #     visit = set()
        #     visit.add((r, c))

        #     while q:
        #         for _ in range(len(q)):
        #             row, col = q.popleft()
        #             if grid[row][col] == 0:
        #                 return level
                    
        #             for dr, dc in directions:
        #                 nr, nc = row + dr, col + dc
        #                 if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visit or grid[nr][nc] == -1:
        #                     continue
        #                 visit.add((nr, nc))
        #                 q.append((nr, nc))
        #         level = level + 1
            
        #     return INF
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == INF:
        #             grid[r][c] = bfs(r, c)
        
            
                
                

                


        