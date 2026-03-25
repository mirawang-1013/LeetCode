class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,0
        left_max=[]
        right_max=[]
        min_max=[]
        drop=0
        for i in range(len(height)):
            left=max(left,height[i])
            left_max.append(left)
        for i in range(len(height)-1,-1,-1):
            right=max(right,height[i])
            right_max.append(right)
        right_max.reverse()
        for i,j in zip(left_max,right_max):
            min_max.append(min(i,j))
        for i,j in zip(min_max,height):
            drop+=(i-j)
        return drop
            