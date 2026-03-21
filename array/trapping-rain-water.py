class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,0
        left_max=[]
        right_max=[]
        min_list=[]
        drop=[]
        for i in range(len(height)):
            left=max(left,height[i])
            left_max.append(left)

        for i in range(len(height)-1,-1,-1):
            right=max(right,height[i])
            right_max.append(right)
        for i,j in zip(left_max,right_max[::-1]):
            print(i,j)
            min_list.append(min(i,j))
        
        for i,j in zip(min_list,height):
          drop.append(i-j)
        return sum(drop)



    
                   
                


        