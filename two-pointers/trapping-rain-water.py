class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=0
        left_max=[0]*len(height)
        right_max=[0]*len(height)
        min_max=[0]*len(height)
        drop=0
        for i in range(len(height)):
            left=max(left,height[i])
            left_max[i]=left
        for i in range(len(height)-1,-1,-1):
            right=max(right,height[i])
            right_max[i]=right
        for i in range(len(height)):
            min_max[i] = min(left_max[i], right_max[i])
        for i in range(len(height)):
            drop+=(min_max[i]-height[i])
        return drop
            