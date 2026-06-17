class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        islands = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == '0':
                return 
            grid[i][j] = '0'
            dfs(i, j+1) # up
            dfs(i, j-1) # down
            dfs(i+1,j) # right
            dfs(i-1,j) # left
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i,j)
                    islands += 1
        return islands