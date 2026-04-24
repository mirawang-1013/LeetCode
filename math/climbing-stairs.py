class Solution:
    def climbStairs(self, n: int) -> int:
#method1
        if n<=2:
            return n
        

        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]



#method2 
        # a = 1
        # b = 2
        # if n<=2:
        #     return n
        # for i in range(3,n+1):
        #     a,b = b, a+b
        # return b