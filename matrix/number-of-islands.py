from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # search if it's ==1
        # use queue to store 1 and explore 4 sides around
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count+=1
                    queue = deque()
                    queue.append([i,j])
                    grid[i][j] = '0'


                    while queue:
                        x,y = queue.popleft()
                        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nx,ny = x+dx, y+dy
                            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                queue.append((nx,ny))
        return count
        
# from typing import List
# from collections import deque

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
        
#         rows = len(grid)
#         cols = len(grid[0])
#         count = 0 # count the number of island

#         #use the bfs and dfs to mark visited land to be 0
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == '1':
#                     count+=1
#                     queue = deque() # to create an empty queue
#                     queue.append([i,j])
#                     grid[i][j] = '0'

#                     while queue:
#                         x,y = queue.popleft() #iterate through the queue
#                         for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#                             nx, ny = x+dx, y+dy
#                             if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == '1':
#                                 grid[nx][ny] = '0'
#                                 queue.append((nx,ny)) #每次检查旁边的4个格子，只要有一个为1，就重新放入后再重新遍历
#         return count