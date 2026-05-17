from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        q=deque()
        fresh=0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c] ==1:
                    fresh+=1
        time=0
        directions=[
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]
        ]

        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    row=r+dr
                    col=c+dc
                
                    if (
                        row < 0 or row >= ROWS or
                        col < 0 or col >= COLS or
                        grid[row][col] != 1
                    ):
                        continue
                    grid[row][col] = 2
                    fresh-=1
                    q.append((row,col))
            time+=1
        if fresh==0:
            return time
        return -1
        