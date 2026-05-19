from typing import List
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        rows=len(grid)
        cols=len(grid[0])
        max_area=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area=0
                    queue=deque()
                    queue.append((i,j))
                    grid[i][j]=0
                
                    while queue:
                        x,y=queue.popleft()
                        area+=1
                        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nx,ny=dx+x,dy+y
                            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] ==1:
                                grid[nx][ny]=0
                                queue.append((nx,ny))
                    max_area=max(area, max_area)
        return max_area


