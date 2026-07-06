class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # cur land: 
        # cur not land: 
        count = 0
        self.grid = grid
        self.c = len(grid[0])
        self.r = len(grid)
        for y in range(self.r):
            for x in range(self.c):
                if self.grid[y][x]=='1':
                    count+=1
                    self.dfs(y,x)
        return count
    
    def dfs(self, x,y):
        if x>=self.r or y>=self.c or x<0 or y<0 or self.grid[x][y] =='0':
            return
        else:
            if self.grid[x][y] =='1': 
                self.grid[x][y] ='0'
            self.dfs(x+1,y)
            self.dfs(x-1,y)
            self.dfs(x,y+1)
            self.dfs(x,y-1)
            return 




