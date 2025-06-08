class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        Len=0
        l=0
        for r in range(len(s)):
            while s[r] in subString:
                subString.remove(s[l])
                l+=1
            subString.add(s[r])
            Len = max(Len,r-l+1)
        return Len
















