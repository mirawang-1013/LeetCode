class Solution:
    def countSubstrings(self, s: str) -> int:
        def extendAroundCenter(left:int, right:int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        result = 0
        for i in range(len(s)):
            result+=extendAroundCenter(i,i)
            result+=extendAroundCenter(i,i+1)
        return result