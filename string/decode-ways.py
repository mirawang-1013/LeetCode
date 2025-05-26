class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': #题目里说了0开头的是invalid code
            return 0
        n = len(s)
        dp = [0]* (n+1)
        #dp[i] 表示：前 i 个字符（下标 0 ~ i-1）的子串，有多少种合法解码方式
        dp[0] = 1 # Base case: empty string has 1 way to decode
        dp[1] = 1

        for i in range(2,n+1):
            one_digit = int(s[i-1])
            two_digit = int(s[i-2:i])

            if 1<=one_digit<=9:
                dp[i]+=dp[i-1]
            
            if 10<=two_digit<=26:
                dp[i] +=dp[i-2]

        return dp[n]
            

