class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #很像接雨水的题目，但是接雨水的是最大，减最小的，得到能接的
        #这个像是临界的，但是取最短的，然后算面积
        area=1*heights[0]
        max_area=area
        for i in range(len(heights)):
            w=i+1
            if len(heights)>1:
                while w<len(heights) and heights[w]>=heights[i]:
                    area=(w-i+1)*heights[i]
                    w+=1
                    max_area=max(max_area,area)
            else:
                max_area=area
               
        return max_area
        