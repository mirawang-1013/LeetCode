from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #initialization: 定义rows, cols, q, fresh
        ROWS=len(grid)
        COLS=len(grid[0])
        q=deque()
        fresh=0

        

        #计算q的队列和fresh，初始化时间，定义directions
        time=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        
        directions=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        #先从队列里取出要作为出发点的橘子，然后开始扩散，注意边界条件不能扩散
        #新鲜橘子会变少，重新标记橘子的编号，调整q的队列
        #注意时间的计算
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()

                for dr, dc in directions:
                    nr=r+dr
                    nc=c+dc

                    if (
                        nr<0 or nr>=ROWS or
                        nc<0 or nc>=COLS or
                        grid[nr][nc]!=1
                    ):
                        continue
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc))
            time+=1
        if fresh==0:
            return time
        return -1
