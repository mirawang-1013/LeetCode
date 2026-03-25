class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #很像接雨水的题目，但是接雨水的是最大，减最小的，得到能接的
        #这个像是临界的，但是取最短的，然后算面积
        stack = [] 
        max_area=0
        for i,h in enumerate(heights):
            start=i
            while stack and h<=stack[-1][1]:
                index,height=stack.pop()
                max_area=max(max_area,height*(i-index))
                start=index
            stack.append((start,h))
        for index,height in stack:
            max_area=max(max_area, (len(heights)-i)*height)
        return max_area
        