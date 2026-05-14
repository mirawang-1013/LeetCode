class Solution:
    def rob(self, nums: List[int]) -> int:
        def robInARow(nums):
            if not nums:
                return 0
            dp=[0]*len(nums)  
            dp[0]=nums[0]
            if len(nums)==1:
                return nums[0]
            dp[1]=max(nums[0],nums[1])
            for n in range(2,len(nums)):
                dp[n]=max(dp[n-1],dp[n-2]+nums[n])
            return dp[-1]
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        return max(robInARow(nums[:-1]),robInARow(nums[1:]))