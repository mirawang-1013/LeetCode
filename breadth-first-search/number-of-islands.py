from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    count+=1
                    queue=collections.deque()
                    queue.append([i,j])
                    grid[i][j]='0'
                    
                    
                
                    while queue:
                        x,y=queue.popleft()
                        for dx,dy in ([-1,0],[1,0],[0,1],[0,-1]):
                            nx,ny=x+dx,y+dy
                            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]=="1":
                                queue.append([nx,ny])
                                grid[nx][ny]=0
        return count
                        
                    





#answer
        # search if it's ==1
        # use queue to store 1 and explore 4 sides around
        # if not grid:
        #     return 0

        # rows = len(grid) # 行数
        # cols = len(grid[0]) #列数
        # count = 0 

        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == '1':
        #             count+=1 #每当走过一个1的时候，count就计数
        #             queue = deque() #令queue等于deque
        #             queue.append([i,j]) #queue把1的坐标放进来
        #             grid[i][j] = '0' #令目前为1的位置为0


        #             while queue: #当queue里有1的坐标
        #                 x,y = queue.popleft() #把坐标pop出来
        #                 for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        #                     #dx,dy是偏移量，也就是上下左右，四个周围的格子
        #                     nx,ny = x+dx, y+dy
        #                     if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == '1': #当偏移的格子还在框里面的时候，且上下左右格子能为1时
        #                         grid[nx][ny] = '0'
        #                         #grid把格子设置为0
        #                         queue.append((nx,ny))#加入队列是准备从这个地方继续扩展
        #                         #然后放进queque
        # return count
        