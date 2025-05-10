class Solution:
    def climbStairs(self, n: int) -> int:
        #当小于两个台阶的时候，那就是One step可以到的事情
        if n<=2:
            return n
        
        #这里先用dp存在来到每一个台阶的可能性
        dp = [0]*(n+1)
        dp[1],dp[2] = 1,2

        #写到n+1才不会只遍历到n就结束了
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]