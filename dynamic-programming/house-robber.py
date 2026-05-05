class Solution:
    def rob(self, nums: List[int]) -> int:
      #if no house here
        if not nums:
            return 0
        dp=[0]*len(num)
        if len(num)==1:
            return num[0]
        if len(num)=2:
            return max(num[0],num[1])
        
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[i-1]