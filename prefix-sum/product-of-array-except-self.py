class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lens = len(nums)
        res = [0]*lens
        left = [0] * lens
        right = [0] * lens
        
        left[0] = 1
        right[lens-1] =1

        for i in range(1,lens):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(lens-2,-1,-1):
            right[i]=right[i+1] * nums[i+1]
        
        for i in range(lens):
            res[i] = left[i]*right[i]
        
        return res

        lens = len(nums)
        res = [0]*lens
        left = [0]*lens
        right = [0]*lens

        #初始化
        left[0]=1
        right[lens-1]=1
        
        #开始计算左边乘积和右边乘积了
        for i in range(1,lens):
            left[i]=left[i-1]*nums[i-1]
        
        for i in range(lens-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        
        for i in range(lens):
            res[i]=left[i]*right[i]
        
        return res