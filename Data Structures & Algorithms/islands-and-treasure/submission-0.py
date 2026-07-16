class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = grid
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j]==0:
                    self.bfs(i,j)
        return

    def bfs(self, a,b):
        queue = deque([(a, b)])
        visited = {(a,b)}
        steps = 1
        while queue: #can still explore
            frontier_size = len(queue)
        
            for i in range(frontier_size): #go thru current frontier
                x,y = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < self.height
                        and 0 <= ny < self.width
                        and (nx, ny) not in visited
                        and self.grid[nx][ny]!=-1
                    ):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        cur = self.grid[nx][ny]
                        if cur!= 0:
                            self.grid[nx][ny] = min(cur, steps)
            steps+=1
        return
                



        # strateg: bfs starting from treasure chest 
#     [
#   [inf,-1,0,inf],
#   [inf,inf,inf,-1],
#   [inf,-1,inf,-1],
#   [0,-1,inf,inf]
# ]
 