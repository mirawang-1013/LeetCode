class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        max_area=0
        while left<right:
            min_height=min(height[left],height[right])
            area=(right-left)*min_height
            max_area=max(max_area,area)
            if height[left]<height[right]:
                    left+=1
            else:
                right-=1
        return max_area













        # left,right=0,len(height)-1
        # max_area=0
        # while left<right:
        #     high=min(height[left],height[right])
        #     max_area=max(max_area,high*(right-left))
        #     if height[left]<height[right]:
        #         left+=1
        #     else:
        #         right-=1
        # return max_area


















        # max_area = 0
        # print(max_area)
        # left, right = 0, len(height)-1
        # while left<right:
        #     print('left',left)
        #     print('right',right)
        #     area = (right-left)* min(height[left],height[right])
        #     max_area = max(max_area,area)
        #     if height[left]<height[right]:
        #         left+=1
        #     else:
        #         right-=1
        # return max_area

        