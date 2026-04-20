class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #大体的思路非常好理解,既然想知道除了这个元素之外的所有乘积
        #那就先把左边的乘积算好，
        #再把右边的乘积算好
        #两边相乘得到答案
        #原来product是乘积的意思
        length = len(nums)
        left = [0]*length
        right = [0]*length
        output = [0]*length

        left[0]=1
        right[length-1]=1

        for i in range(1,length):
            left[i]=left[i-1]*nums[i-1]

        
        for i in range(length-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        
        for i in range(length):
            output[i] = left[i]*right[i]
        return output











        # lens = len(nums)
        # res = [0]*lens
        # left = [0] * lens
        # right = [0] * lens
        
        # left[0] = 1
        # right[lens-1] =1

        # for i in range(1,lens):
        #     left[i] = left[i-1] * nums[i-1]
        
        # for i in range(lens-2,-1,-1):
        #     right[i]=right[i+1] * nums[i+1]
        
        # for i in range(lens):
        #     res[i] = left[i]*right[i]
        
        # return res

        # lens = len(nums)
        # res = [0]*lens
        # left = [0]*lens
        # right = [0]*lens

        # #初始化
        # left[0]=1
        # right[lens-1]=1
        
        # #开始计算左边乘积和右边乘积了
        # for i in range(1,lens):
        #     left[i]=left[i-1]*nums[i-1]
        
        # for i in range(lens-2,-1,-1):
        #     right[i]=right[i+1]*nums[i+1]
        
        # for i in range(lens):
        #     res[i]=left[i]*right[i]
        
        # return res