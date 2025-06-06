class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        #创造个二维的DP表
        dp = [[0]*(n+1) for _ in range(m+1)]

        # 初始化第一行和第一列（一个字符串为空时）
        for i in range(m + 1):
            dp[i][0] = i  # 删除操作
        for j in range(n + 1):
            dp[0][j] = j  # 插入操作
        
        #填表
        for i in range(1,m+1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 无需操作
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # 删除
                        dp[i][j - 1],    # 插入
                        dp[i - 1][j - 1] # 替换
                    )

        return dp[m][n]

        