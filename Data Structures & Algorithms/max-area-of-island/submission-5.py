class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
        self.max = 0
        self.count = 0
        #loops through the grid
        for x in range(self.height):
            for y in range(self.width):
                self.dfs(x,y)
                self.count=0

                # print(self.max)

        return self.max

    def dfs(self, x, y):
        #sees zero: do nothing
        if x<0 or y<0 or x>=self.height or y>=self.width or self.grid[x][y] ==0:
            # print("zero")
            return
        #sees one: add 1 to area
        self.count +=1

        print(f"{x}, {y}, {self.count}.")
        # print(self.count)
        
        if self.count>self.max:
            self.max = self.count

        self.grid[x][y]=0
        self.dfs(x+1, y)
        self.dfs(x-1, y)

        self.dfs(x, y-1)
        self.dfs(x,y+1)

        #all branches have done, no more connecting land --> reset count to zero
        return 

    #  0,1,2,3,4,5,6,7,8,9,0,1,2
  #[[0,0,1,0,0,0,0,1,0,0,0,0,0]0
  #,[0,0,0,0,0,0,0,1,1,1,0,0,0]1
  #,[0,1,1,0,1,0,0,0,0,0,0,0,0]2
  #,[0,1,0,0,1,1,0,0,1,0,1,0,0]3
  #,[0,1,0,0,1,1,0,0,1,1,1,0,0]4
  #,[0,0,0,0,0,0,0,0,0,0,1,0,0]5
  #,[0,0,0,0,0,0,0,1,1,1,0,0,0]6
  #,[0,0,0,0,0,0,0,1,1,0,0,0,0]7                 
