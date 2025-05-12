class Solution:
    def rob(self, nums: List[int]) -> int:
      #if no house here
        if not nums:
            return 0
        if len(nums) ==1:
            return nums[0]


        dp=[0]* len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
        #不抢当前这个，那就是dp[i-1]
        #抢当前这个，那就是dp[i-2] + nums[i]
            dp[i] = max(dp[i-1],dp[i-2]+nums[i]) 

        return dp[-1]   