class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        def max(height:List[int])->int:
            if len(height)==1:
                return height[0]
            else:
                tmp = max(height[1:])
                return height[0] if height[0]>tmp else tmp
        for i in range(len(height)):
            lMax = max(height[:i]+[0])
            rMax = max(height[i+1:]+[0])
            bound = min(lMax,rMax)
            if bound>height[i]:
                total = total+(bound-height[i])
        return total 








        # if not height:
        #     return 0
        
        # left, right = 0, len(height)-1 #初始化左右两个指针
        # left_max,right_max = 0,0  # 记录左右两边的最大高度
        # water_trapped = 0

        # while left<right: #左指针和右指针还没有相遇的时候
        # #若左指针的高度小于右指针的高度
        #     if height[left]<height[right]:
        #         if height[left]>=left_max:
        #             #如果这个height是最高的，那么left_max的值要更新一下
        #             left_max = height[left]
        #         else:
        #             water_trapped += left_max-height[left]
        #         left+=1
        #     else:
        #         if height[right]>=right_max:
        #             right_max=height[right]
        #         else:
        #             water_trapped += right_max-height[right]
        #         right -=1
        # return water_trapped
            
            
                


        